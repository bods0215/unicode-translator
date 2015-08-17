#!/usr/bin/env python

import sys
import random

transform = {}

# Latin Extended A
letterRange = lambda b, e: [chr(i) for i in range(b, e)]

# transform['a'] = [chr(i) for i in range(0x100, 0x105)]
transform['a'] = letterRange(0x100, 0x105)
transform['c'] = letterRange(0x106, 0x10D)
transform['d'] = letterRange(0x10E, 0x111)
transform['e'] = letterRange(0x112, 0x11B)
transform['g'] = letterRange(0x11C, 0x123)
transform['h'] = letterRange(0x124, 0x127)
transform['i'] = letterRange(0x128, 0x133)
transform['j'] = letterRange(0x134, 0x135)
transform['k'] = letterRange(0x136, 0x138)
transform['l'] = letterRange(0x139, 0x142)
transform['n'] = letterRange(0x143, 0x14B)
transform['o'] = letterRange(0x14C, 0x153)
transform['r'] = letterRange(0x154, 0x159)
transform['s'] = letterRange(0x15A, 0x161)
transform['s'].append(chr(0x017f))
transform['t'] = letterRange(0x162, 0x167)
transform['u'] = letterRange(0x168, 0x173)
transform['w'] = letterRange(0x174, 0x175)
transform['y'] = letterRange(0x176, 0x178)
transform['z'] = letterRange(0x179, 0x17d)


outputStr = []

inputStr = sys.argv[1]

for c in inputStr:
    if c in transform:
        unicodeChars = transform[c]
        r = random.randint(0, len(unicodeChars)-1)
        outputStr.append(transform[c][r])
    else:
        outputStr.append(c)

print(''.join(outputStr))
