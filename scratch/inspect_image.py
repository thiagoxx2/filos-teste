import struct
import zlib

def test_tolerances(path):
    print(f"Testing tolerances for PNG: {path}")
    try:
        with open(path, 'rb') as f:
            sig = f.read(8)
            if sig != b'\x89PNG\r\n\x1a\n': return
            idat_data = b''
            width, height = 0, 0
            while True:
                len_bytes = f.read(4)
                if not len_bytes: break
                length, = struct.unpack('>I', len_bytes)
                ctype = f.read(4).decode('ascii')
                data = f.read(length)
                f.read(4)
                if ctype == 'IHDR':
                    width, height, depth, color_type, compress, filter_m, interlace = struct.unpack('>IIBBBBB', data)
                elif ctype == 'IDAT':
                    idat_data += data
                elif ctype == 'IEND':
                    break
            
            if color_type != 6: return
            decompressed = zlib.decompress(idat_data)
            scanline_len = 1 + width * 4
            row_size = width * 4
            recon_original = bytearray(height * row_size)
            for r in range(height):
                scanline = decompressed[r * scanline_len : (r + 1) * scanline_len]
                ftype = scanline[0]
                for c in range(row_size):
                    filt_x = scanline[1 + c]
                    recon_a = recon_original[r * row_size + c - 4] if c >= 4 else 0
                    recon_b = recon_original[(r - 1) * row_size + c] if r > 0 else 0
                    recon_c = recon_original[(r - 1) * row_size + c - 4] if (r > 0 and c >= 4) else 0
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
                    recon_original[r * row_size + c] = recon_x

        def get_pixel(recon, x, y):
            idx = (y * width + x) * 4
            return (recon[idx], recon[idx+1], recon[idx+2], recon[idx+3])

        target_color = get_pixel(recon_original, 0, 0)
        
        # Test tolerance from 25 to 55 in steps of 5
        for tolerance in range(25, 60, 5):
            recon = bytearray(recon_original)
            visited = set()
            from collections import deque
            queue = deque()
            
            def color_dist(c1, c2):
                return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5
                
            # Queue edge pixels
            for x in range(width):
                for y in [0, height - 1]:
                    if (x, y) not in visited:
                        c = get_pixel(recon, x, y)
                        if color_dist(c, target_color) < tolerance:
                            queue.append((x, y))
                            visited.add((x, y))
            for y in range(height):
                for x in [0, width - 1]:
                    if (x, y) not in visited:
                        c = get_pixel(recon, x, y)
                        if color_dist(c, target_color) < tolerance:
                            queue.append((x, y))
                            visited.add((x, y))
            
            # BFS flood fill
            changed = 0
            while queue:
                x, y = queue.popleft()
                # Set alpha to 0
                idx = (y * width + x) * 4
                recon[idx+3] = 0
                changed += 1
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        if (nx, ny) not in visited:
                            c = get_pixel(recon, nx, ny)
                            if color_dist(c, target_color) < tolerance:
                                visited.add((nx, ny))
                                queue.append((nx, ny))
            
            # Check edge alphas
            top_opaque = 0
            bottom_opaque = 0
            for x in range(width):
                if recon[(0*width + x)*4 + 3] > 0: top_opaque += 1
                if recon[((height-1)*width + x)*4 + 3] > 0: bottom_opaque += 1
            print(f"Tol {tolerance}: Changed {changed} pixels. Top opaque: {top_opaque}/{width}, Bottom opaque: {bottom_opaque}/{width}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_tolerances("assets/images/vestibular-student-card.png")
