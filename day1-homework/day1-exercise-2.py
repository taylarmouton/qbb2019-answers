#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
counter = 0
for line in in_file:
    if "NM:i:0" in line:
        counter += 1
print(counter)
        
