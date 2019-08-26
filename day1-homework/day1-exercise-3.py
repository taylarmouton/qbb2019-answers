#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
counter = 0
for line in in_file:
    fields = line.strip().split("\t")
    if "NH:i:1" in fields[11:]:
        counter += 1
print(counter)