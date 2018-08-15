#!/usr/bin/env python3

import png

with open("ULT/CHUNKS", "rb") as f:
    data = f.read()
    chunks = []
    for chunk_num in range(1024):
        chunk = []
        for y in range(8):
            row = []
            for x in range(8):
                offset = 64 * chunk_num + 8 * y + x
                d = data[offset]
                row.append(d)
            chunk.append(row)
        chunks.append(chunk)

with open("ULT/MAP", "rb") as f:
    britannia = []
    for yy in range(8):
        britannia_row = []
        for xx in range(8):
            block = []
            for y in range(16):
                row = []
                for x in range(8):
                    a, b, c = f.read(3)
                    d, e = divmod(c * 256 * 256 + b * 256 + a, 4096)
                    row.append(e)
                    row.append(d)
                block.append(row)
            britannia_row.append(block)
        britannia.append(britannia_row)

pixels = []
for yy in range(8):
    for y in range(16):
        for cy in range(8):
            for xx in range(8):
                for x in range(16):
                    for cx in range(8):
                        tile = chunks[britannia[yy][xx][y][x]][cy][cx]
                        r, gb = divmod(tile, 64)
                        g, b = divmod(gb, 4)
                        pixels.append((r << 6, g << 4, b << 6))
png.write_png("map.png", 1024, 1024, pixels)
