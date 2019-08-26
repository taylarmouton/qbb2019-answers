#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
counter = 0
total_MAPQ = 0
for line in in_file:
    fields = line.strip().split("\t")
    counter += 1
    total_MAPQ += int(fields[4])
avg = float(total_MAPQ) / float(counter)
print(avg)
    
    