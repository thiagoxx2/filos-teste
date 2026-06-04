import sys
import struct
import zlib

def process_png(img_path, output_path):
    print(f"Reading PNG: {img_path}")
    with open(img_path, 'rb') as f:
        sig = f.read(8)
        if sig != b'\x89PNG\r\n\x1a\n':
            raise ValueError("Not a valid PNG file.")
            
        chunks = []
        idat_data = b''
        width = 0
        height = 0
        
        while True:
            len_bytes = f.read(4)
            if not len_bytes:
                break
            length, = struct.unpack('>I', len_bytes)
            ctype = f.read(4).decode('ascii')
            data = f.read(length)
            crc = f.read(4)
            
            if ctype == 'IHDR':
                width, height, depth, color_type, compress, filter_m, interlace = struct.unpack('>IIBBBBB', data)
                if color_type != 6 or depth != 8:
                    raise ValueError(f"Only 8-bit RGBA PNGs (color type 6) are supported. Got type={color_type}, depth={depth}")
            elif ctype == 'IDAT':
                idat_data += data
            elif ctype == 'IEND':
                break
                
    print(f"Loaded image size: {width}x{height}")
    
    # Decompress IDAT
    decompressed = zlib.decompress(idat_data)
    scanline_len = 1 + width * 4
    row_size = width * 4
    
    if len(decompressed) != height * scanline_len:
        raise ValueError(f"Decompressed data size mismatch: {len(decompressed)} vs {height * scanline_len}")
        
    # Unfilter scanlines
    print("Unfiltering scanlines...")
    recon = bytearray(height * row_size)
    for r in range(height):
        scanline = decompressed[r * scanline_len : (r + 1) * scanline_len]
        ftype = scanline[0]
        for c in range(row_size):
            filt_x = scanline[1 + c]
            recon_a = recon[r * row_size + c - 4] if c >= 4 else 0
            recon_b = recon[(r - 1) * row_size + c] if r > 0 else 0
            recon_c = recon[(r - 1) * row_size + c - 4] if (r > 0 and c >= 4) else 0
            
            if ftype == 0:
                recon_x = filt_x
            elif ftype == 1:
                recon_x = (filt_x + recon_a) % 256
            elif ftype == 2:
                recon_x = (filt_x + recon_b) % 256
            elif ftype == 3:
                recon_x = (filt_x + (recon_a + recon_b) // 2) % 256
            elif ftype == 4:
                # Paeth
                p = recon_a + recon_b - recon_c
                pa = abs(p - recon_a)
                pb = abs(p - recon_b)
                pc = abs(p - recon_c)
                if pa <= pb and pa <= pc:
                    pred = recon_a
                elif pb <= pc:
                    pred = recon_b
                else:
                    pred = recon_c
                recon_x = (filt_x + pred) % 256
            else:
                raise ValueError(f"Unknown filter type: {ftype}")
                
            recon[r * row_size + c] = recon_x
            
    # Flood-fill background pixels (convert matching dark blue pixels to fully transparent)
    def get_pixel(x, y):
        idx = (y * width + x) * 4
        return (recon[idx], recon[idx+1], recon[idx+2], recon[idx+3])
        
    def set_pixel(x, y, color):
        idx = (y * width + x) * 4
        recon[idx] = color[0]
        recon[idx+1] = color[1]
        recon[idx+2] = color[2]
        recon[idx+3] = color[3]
        
    target_color = get_pixel(0, 0)
    print(f"Detecting background color at (0,0): {target_color}")
    
    # We want to remove colors matching the dark blue background
    # Target background in mockup is typically around (13, 27, 42)
    # We will start flood fill from the borders
    visited = set()
    from collections import deque
    queue = deque()
    
    tolerance = 25  # Color distance threshold
    def color_dist(c1, c2):
        return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5
        
    # Queue edge pixels
    for x in range(width):
        for y in [0, height - 1]:
            if (x, y) not in visited:
                c = get_pixel(x, y)
                if color_dist(c, target_color) < tolerance:
                    queue.append((x, y))
                    visited.add((x, y))
                    
    for y in range(height):
        for x in [0, width - 1]:
            if (x, y) not in visited:
                c = get_pixel(x, y)
                if color_dist(c, target_color) < tolerance:
                    queue.append((x, y))
                    visited.add((x, y))
                    
    # BFS flood-fill
    changed = 0
    while queue:
        x, y = queue.popleft()
        # Set alpha to 0 (make transparent)
        set_pixel(x, y, (0, 0, 0, 0))
        changed += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    c = get_pixel(nx, ny)
                    if color_dist(c, target_color) < tolerance:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        
    print(f"Made {changed} background pixels transparent.")
    
    # Compress back with filter type 0 (None)
    print("Compressing image data...")
    new_decompressed = bytearray(height * scanline_len)
    for r in range(height):
        new_decompressed[r * scanline_len] = 0 # Filter type 0
        new_decompressed[r * scanline_len + 1 : (r + 1) * scanline_len] = recon[r * row_size : (r + 1) * row_size]
        
    new_idat_data = zlib.compress(new_decompressed)
    
    # Write new PNG
    print(f"Writing PNG: {output_path}")
    with open(output_path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        
        # Write IHDR
        ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
        write_chunk(f, 'IHDR', ihdr_data)
        
        # Write IDAT
        write_chunk(f, 'IDAT', new_idat_data)
        
        # Write IEND
        write_chunk(f, 'IEND', b'')
        
    print("Done!")

def write_chunk(f, ctype, data):
    length = len(data)
    f.write(struct.pack('>I', length))
    f.write(ctype.encode('ascii'))
    f.write(data)
    crc = zlib.crc32(ctype.encode('ascii') + data) & 0xffffffff
    f.write(struct.pack('>I', crc))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 process_png.py <input_path> <output_path>")
        sys.exit(1)
    process_png(sys.argv[1], sys.argv[2])
