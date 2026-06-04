import struct
import zlib
import sys

def process_png_advanced(img_path, output_path, tolerance=20):
    print(f"Reading PNG: {img_path}")
    with open(img_path, 'rb') as f:
        sig = f.read(8)
        if sig != b'\x89PNG\r\n\x1a\n':
            raise ValueError("Not a valid PNG file.")
            
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
    
    decompressed = zlib.decompress(idat_data)
    scanline_len = 1 + width * 4
    row_size = width * 4
    
    # Unfilter scanlines
    recon = bytearray(height * row_size)
    for r in range(height):
        scanline = decompressed[r * scanline_len : (r + 1) * scanline_len]
        ftype = scanline[0]
        for c in range(row_size):
            filt_x = scanline[1 + c]
            recon_a = recon[r * row_size + c - 4] if c >= 4 else 0
            recon_b = recon[(r - 1) * row_size + c] if r > 0 else 0
            recon_c = recon[(r - 1) * row_size + c - 4] if (r > 0 and c >= 4) else 0
            
            if ftype == 0: recon_x = filt_x
            elif ftype == 1: recon_x = (filt_x + recon_a) % 256
            elif ftype == 2: recon_x = (filt_x + recon_b) % 256
            elif ftype == 3: recon_x = (filt_x + (recon_a + recon_b) // 2) % 256
            elif ftype == 4:
                p = recon_a + recon_b - recon_c
                pa = abs(p - recon_a)
                pb = abs(p - recon_b)
                pc = abs(p - recon_c)
                if pa <= pb and pa <= pc: pred = recon_a
                elif pb <= pc: pred = recon_b
                else: pred = recon_c
                recon_x = (filt_x + pred) % 256
            recon[r * row_size + c] = recon_x
            
    def get_pixel(x, y):
        idx = (y * width + x) * 4
        return (recon[idx], recon[idx+1], recon[idx+2], recon[idx+3])
        
    def set_pixel(x, y, color):
        idx = (y * width + x) * 4
        recon[idx] = color[0]
        recon[idx+1] = color[1]
        recon[idx+2] = color[2]
        recon[idx+3] = color[3]

    # Collect seed background colors from SAFE border regions
    bg_seeds = []
    
    # Left and Right edges (x=0, x=width-1) are completely background
    for y in range(height):
        bg_seeds.append(get_pixel(0, y)[:3])
        bg_seeds.append(get_pixel(width - 1, y)[:3])
        
    # Top edge (y=0) except the center region where the boy's hair is
    for x in range(width):
        if x < 250 or x > width - 250:
            bg_seeds.append(get_pixel(x, 0)[:3])
            
    # Remove duplicates
    bg_seeds = list(set(bg_seeds))
    print(f"Collected {len(bg_seeds)} unique background seed colors from SAFE borders.")
    
    # BFS flood-fill
    visited = set()
    from collections import deque
    queue = deque()
    
    def color_dist(c1, c2):
        return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5
        
    def is_background(color):
        for seed in bg_seeds:
            if color_dist(color, seed) < tolerance:
                return True
        return False
        
    # Add initial border pixels to queue (only from safe regions)
    for x in range(width):
        # Top edge
        if x < 250 or x > width - 250:
            c = get_pixel(x, 0)
            if is_background(c[:3]):
                queue.append((x, 0))
                visited.add((x, 0))
        # Bottom edge corners (near left and right)
        if x < 40 or x > width - 40:
            c = get_pixel(x, height - 1)
            if is_background(c[:3]):
                queue.append((x, height - 1))
                visited.add((x, height - 1))
                
    for y in range(height):
        # Left edge
        c = get_pixel(0, y)
        if is_background(c[:3]) and (0, y) not in visited:
            queue.append((0, y))
            visited.add((0, y))
        # Right edge
        c = get_pixel(width - 1, y)
        if is_background(c[:3]) and (width - 1, y) not in visited:
            queue.append((width - 1, y))
            visited.add((width - 1, y))
                    
    # Run BFS
    changed = 0
    while queue:
        x, y = queue.popleft()
        set_pixel(x, y, (0, 0, 0, 0))
        changed += 1
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    c = get_pixel(nx, ny)
                    if is_background(c[:3]):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        
    print(f"Made {changed} pixels transparent.")
    
    # Check top row opacities
    top_opaque = 0
    for x in range(width):
        if recon[(0*width + x)*4 + 3] > 0:
            top_opaque += 1
    print(f"Post-processing top opaque pixels: {top_opaque} / {width}")
    
    # Compress and write
    print("Compressing image data...")
    new_decompressed = bytearray(height * scanline_len)
    for r in range(height):
        new_decompressed[r * scanline_len] = 0
        new_decompressed[r * scanline_len + 1 : (r + 1) * scanline_len] = recon[r * row_size : (r + 1) * row_size]
        
    new_idat_data = zlib.compress(new_decompressed)
    
    print(f"Writing PNG: {output_path}")
    with open(output_path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
        write_chunk(f, 'IHDR', ihdr_data)
        write_chunk(f, 'IDAT', new_idat_data)
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
    tolerance = 20
    if len(sys.argv) > 3:
        tolerance = float(sys.argv[3])
    process_png_advanced(sys.argv[1], sys.argv[2], tolerance)
