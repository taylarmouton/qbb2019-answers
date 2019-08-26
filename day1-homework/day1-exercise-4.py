#!/usr/bin/env python3

import sys

in_file = open(sys.argv[1])
for i, line in enumerate(in_file):
    if i >= 10:
        break
    line = line.rstrip("\n")
    fields = line.split("\t")
    print(fields[2])    