#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
counter = 0
for line in in_file: 
    fields = line.split("\t")
    if fields[2] == "*":
        continue
    counter += 1
    #count = count + 1
print(counter)

