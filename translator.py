#!/usr/bin/env python

import sys
import random

latinextendeda = {}

# Latin Extended A
letterRange = lambda b, e: [chr(i) for i in range(b, e)]

# latinextendeda['a'] = [chr(i) for i in range(0x100, 0x105)]
latinextendeda['a'] = letterRange(0x100, 0x105)
latinextendeda['c'] = letterRange(0x106, 0x10D)
latinextendeda['d'] = letterRange(0x10E, 0x111)
latinextendeda['e'] = letterRange(0x112, 0x11B)
latinextendeda['g'] = letterRange(0x11C, 0x123)
latinextendeda['h'] = letterRange(0x124, 0x127)
latinextendeda['i'] = letterRange(0x128, 0x133)
latinextendeda['j'] = letterRange(0x134, 0x135)
latinextendeda['k'] = letterRange(0x136, 0x138)
latinextendeda['l'] = letterRange(0x139, 0x142)
latinextendeda['n'] = letterRange(0x143, 0x14B)
latinextendeda['o'] = letterRange(0x14C, 0x153)
latinextendeda['r'] = letterRange(0x154, 0x159)
latinextendeda['s'] = letterRange(0x15A, 0x161)
latinextendeda['s'].append(chr(0x017f))
latinextendeda['t'] = letterRange(0x162, 0x167)
latinextendeda['u'] = letterRange(0x168, 0x173)
latinextendeda['w'] = letterRange(0x174, 0x175)
latinextendeda['y'] = letterRange(0x176, 0x178)
latinextendeda['z'] = letterRange(0x179, 0x17d)

outputStr = []

inputStr = sys.argv[1]

for c in inputStr.lower():
    if c in latinextendeda:
        chars = latinextendeda[c]
        r = random.randint(0, len(chars)-1)
        outputStr.append(chars[r])
    else:
        outputStr.append(c)

print(inputStr)
print(''.join(outputStr))
