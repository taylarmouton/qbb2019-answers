#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
count = 0
for line in in_file:
    fields = line.strip().split("\t")
    if fields[2] == "2L":
        if 20000 >= int(fields[3]) >= 10000:
            count += 1
print(count)
             