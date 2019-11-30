#!/usr/bin/env python3

with open("var.vcf") as f:
    for line in f:
        if "##" in line:
            continue
        print(line)