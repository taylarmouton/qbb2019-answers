#!/usr/bin/env python3

""""
Binary search to locate mutations in BDGP6.Ensembl.81.gtf
"""
import sys

chr_3R = []
f = open(sys.argv[1])
#count = 0

#opening out file from Exercise 1
for i, line in enumerate(f):
    columns = line.rstrip("\n").split()
    if line.startswith("#"):
        continue
    if "3R" in columns[0] and "gene" in columns[2] and 'gene_biotype "protein_coding"' in line:
        gene = int(columns[3]), int(columns[4]), (columns[13])
        chr_3R.append(gene)
        # count += 1
# print(chr_3R)
#print(count)

search_chr = "3R"
search_pos = 21378950
lo = 0
hi = len(chr_3R)-1
mid = 0
number_iterations = 0

while (lo <= hi):
    mid = int((hi+lo) / 2)
    # print(lo,mid,hi)
    if hi == mid or lo == mid:
        break
    number_iterations = number_iterations + 1
    if (search_pos < chr_3R[mid][0]):
        hi = mid 
    elif (search_pos > chr_3R[mid][1]):
        lo = mid 
    else:
        # chr_3R[mid]
        break

print(chr_3R[mid][2])


    