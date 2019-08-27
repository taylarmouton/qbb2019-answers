#!/usr/bin/env python3

""""
Count transcripts of selected genes from a t_data.ctab file

usage ./02-count-goi.py <gene name file> <gtf>
"""

import sys

genes_of_interest = set()
for line in open(sys.argv[1]):
    genes_of_interest.add(line.strip())
    
gene_name_counts = {}

for i, line in enumerate(sys.stdin):
    #ignore the header on first line
    if i == 0:
        continue
    #get gene name
    columns = line.rstrip("\n").split("\t")
    gene_name = columns[9]
    if gene_name not in genes_of_interest:
        continue
    #And gene if not seen before
    if gene_name in gene_name_counts:
        gene_name_counts[gene_name] += 1 
    else:
        gene_name_counts[gene_name] = 1
        
for name in gene_name_counts:
        print(name, gene_name_counts[name])