#!/usr/bin/env python3


with open("ULT/MAP", "rb") as f:

    ## britannia
    
    # 8 x 8 blocks
    for yy in range(8):
        for xx in range(8):
            print()
            print(f"block {xx}, {yy}:")
            # each of 16 x 16 chunks
            for y in range(16):
                for x in range(8):
                    a, b, c = f.read(3)
                    d, e = divmod(c * 256 * 256 + b * 256 + a, 4096)
                    print(f"{d:04X}", end=" ")
                    print(f"{e:04X}", end=" ")
                print()
