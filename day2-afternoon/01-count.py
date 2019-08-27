#!/usr/bin/env python3

""""
Count transcripts per gene from a t_data.ctab
"""

import sys


gene_name_counts = {}

for i, line in enumerate(sys.stdin):
    #ignore the header on first line
    if i == 0:
        continue
    #get gene name
    columns = line.rstrip("\n").split("\t")
    gene_name = columns[9]
    #And gene if not seen before
    if gene_name in gene_name_counts:
        gene_name_counts[gene_name] += 1 
    else:
        gene_name_counts[gene_name] = 1
        
for name in gene_name_counts:
        print(name, gene_name_counts[name])