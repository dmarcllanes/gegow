"""Run once: python make_icons.py — generates static/icons/icon-192.png and icon-512.png"""
import struct, zlib, os

def png(size, bg=(13, 148, 136), fg=(255,255,255)):
    """Generate a minimal solid-color PNG with a white 'G' letter."""
    # Build raw image data (RGBA)
    pixels = []
    cx, cy = size // 2, size // 2
    r = size * 0.28  # letter radius
    stroke = max(size // 22, 2)

    for y in range(size):
        row = []
        for x in range(size):
            # Background circle on teal square
            dx, dy = x - cx, y - cy
            dist = (dx*dx + dy*dy) ** 0.5
            # Simple 'G' letter approximation using pixel art logic
            # Outer circle
            in_outer = dist < r
            in_inner = dist < r - stroke
            # Right side gap (top-right quadrant — open part of G)
            angle_ok = not (dx > 0 and abs(dy) < r * 0.18)
            # Horizontal bar (middle right of G)
            in_bar = (dx > 0 and dx < r and abs(dy - r * 0.05) < stroke * 0.9)

            if in_outer and (not in_inner or in_bar) and (angle_ok or in_bar):
                row += list(fg) + [255]
            else:
                row += list(bg) + [255]
        pixels.append(bytes(row))

    def chunk(name, data):
        c = struct.pack('>I', len(data)) + name + data
        return c + struct.pack('>I', zlib.crc32(name + data) & 0xffffffff)

    raw = b''.join(b'\x00' + row for row in pixels)
    idat = zlib.compress(raw, 9)

    return (
        b'\x89PNG\r\n\x1a\n'
        + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
        + chunk(b'IDAT', idat)
        + chunk(b'IEND', b'')
    )

os.makedirs('static/icons', exist_ok=True)
for size in (192, 512):
    path = f'static/icons/icon-{size}.png'
    with open(path, 'wb') as f:
        f.write(png(size))
    print(f'Created {path}')
