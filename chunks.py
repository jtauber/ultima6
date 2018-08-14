#!/usr/bin/env python3

with open("ULT/CHUNKS", "rb") as f:
    data = f.read()
    assert len(data) == 65536
    # 1024 chunks each of 64 bytes 8 x 8
    for chunk_num in range(1024):
        print()
        print(f"chunk {chunk_num}:")
        for y in range(8):
            for x in range(8):
                offset = 64 * chunk_num + 8 * y + x
                print(f"{data[offset]:02X}", end=" ")
            print()
