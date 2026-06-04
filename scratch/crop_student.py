import os
import struct
import zlib

def crop_png(img_path):
    print(f"Reading image to crop: {img_path}")
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return
        
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
            f.read(4) # CRC
            
            if ctype == 'IHDR':
                width, height, depth, color_type, compress, filter_m, interlace = struct.unpack('>IIBBBBB', data)
                if color_type != 6 or depth != 8:
                    raise ValueError(f"Only 8-bit RGBA PNGs (color type 6) are supported. Got type={color_type}, depth={depth}")
            elif ctype == 'IDAT':
                idat_data += data
            elif ctype == 'IEND':
                break
                
    # Decompress IDAT
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
            
            if ftype == 0:
                recon_x = filt_x
            elif ftype == 1:
                recon_x = (filt_x + recon_a) % 256
            elif ftype == 2:
                recon_x = (filt_x + recon_b) % 256
            elif ftype == 3:
                recon_x = (filt_x + (recon_a + recon_b) // 2) % 256
            elif ftype == 4:
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
            recon[r * row_size + c] = recon_x
            
    # Find bounding box of non-transparent pixels (alpha > 0)
    min_x, max_x = width, 0
    min_y, max_y = height, 0
    
    for y in range(height):
        for x in range(width):
            idx = (y * width + x) * 4
            a = recon[idx + 3]
            if a > 0:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    if min_x > max_x or min_y > max_y:
        print("Image is entirely transparent, no crop needed.")
        return
        
    print(f"Bounding box: X from {min_x} to {max_x}, Y from {min_y} to {max_y}")
    new_w = max_x - min_x + 1
    new_h = max_y - min_y + 1
    print(f"New cropped size: {new_w}x{new_h}")
    
    # Create cropped data
    cropped_recon = bytearray(new_h * new_w * 4)
    for y in range(new_h):
        for x in range(new_w):
            old_idx = ((min_y + y) * width + (min_x + x)) * 4
            new_idx = (y * new_w + x) * 4
            cropped_recon[new_idx : new_idx + 4] = recon[old_idx : old_idx + 4]
            
    # Compress back with filter type 0 (None)
    new_decompressed = bytearray(new_h * (1 + new_w * 4))
    for r in range(new_h):
        new_decompressed[r * (1 + new_w * 4)] = 0 # filter type 0
        new_decompressed[r * (1 + new_w * 4) + 1 : (r + 1) * (1 + new_w * 4)] = cropped_recon[r * new_w * 4 : (r + 1) * new_w * 4]
        
    new_idat = zlib.compress(new_decompressed)
    
    # Write cropped PNG back
    print(f"Writing cropped PNG back to: {img_path}")
    with open(img_path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        # IHDR
        ihdr_data = struct.pack('>IIBBBBB', new_w, new_h, 8, 6, 0, 0, 0)
        write_chunk(f, 'IHDR', ihdr_data)
        # IDAT
        write_chunk(f, 'IDAT', new_idat)
        # IEND
        write_chunk(f, 'IEND', b'')
    print("Crop complete!")

def write_chunk(f, ctype, data):
    length = len(data)
    f.write(struct.pack('>I', length))
    f.write(ctype.encode('ascii'))
    f.write(data)
    crc = zlib.crc32(ctype.encode('ascii') + data) & 0xffffffff
    f.write(struct.pack('>I', crc))

if __name__ == "__main__":
    crop_png("/Users/shayenefreita/FACULDADE FILOS/assets/images/student-pink-isolated.png")
    crop_png("/Users/shayenefreita/FACULDADE FILOS/assets/images/student-portrait.png")
    crop_png("/Users/shayenefreita/FILOS TESTE 2/assets/images/student-pink-isolated.png")
    crop_png("/Users/shayenefreita/FILOS TESTE 2/assets/images/student-portrait.png")
