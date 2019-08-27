#!/usr/bin/env python3

""""
Print all unique gene names from a t_data.ctab file
"""

import sys

#gene_names_seen = []
#gene_names_seen = {}
gene_names_seen = set()
for i, line in enumerate(sys.stdin):
    #ignore the header on first line
    if i == 0:
        continue
    #get gene name
    columns = line.rstrip("\n").split("\t")
    gene_name = columns[9]
    #And gene if not seen before
    if gene_name in gene_names_seen:
        continue 
    else:
        #gene_names_seen.append(gene_name)
        #gene_names_seen[gene_name] = True
        gene_names_seen.add(gene_name)
        
for name in gene_names_seen:
        print(name)