#!/usr/bin/env python3
import re

fh = open("input.txt", 'r')

s = 0
for line in fh:
    line = line.strip()
    line = re.sub(r'\D', '', line)
    s += int(line[0] + line[-1])
    
print(f"Solution {s}")