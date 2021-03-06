#!/usr/bin/env python3

""""
Binary search to locate mutations in BDGP6.Ensembl.81.gtf
"""
import sys

chr_3R = []
chr_3R_dict = {}
f = open(sys.argv[1])
#count = 0
        
#opening out file from Exercise 1
for i, line in enumerate(f):
    columns = line.rstrip("\n").split()
    if line.startswith("#"):
        continue
    if "3R" in columns[0] and "gene" in columns[2] and 'gene_biotype "protein_coding"' in line:
        chr_3R.append(int( columns[3]))
        chr_3R.append(int( columns[4]))
        gene_name = columns[13]
        chr_3R_dict[columns[3]] = gene_name
        chr_3R_dict[columns[4]] = gene_name
        # gene = int(columns[3]), int(columns[4]), (columns[13])
#         chr_3R_dict[(columns[3]), int(columns[4]))] = gene
#         chr_3R.append(gene)
        #count += 1
# print(chr_3R)
#print(count)

#search_chr = "3R"
search_pos = 21378950
lo = 0
hi = len(chr_3R)-1
mid = 0
iteration = 0

while hi > 1:
    hi = len(chr_3R) - 1
    iteration += 1
    mid = int((hi+lo) / 2)
    if chr_3R[mid] == search_pos:
        gene_pos = chr_3R[mid]
        gene_name = chr_3R_dict[str(gene_pos)]
        print(gene_name, abs(chr_3R[mid][2] - search_pos), iteration)
    elif chr_3R[mid] > search_pos:
        chr_3R = chr_3R[:mid] 
    elif (search_pos > chr_3R[mid]):
        chr_3R = chr_3R[mid:] 
    else:
        break
        

gene_pos = chr_3R[mid]
gene_name = chr_3R_dict[str(gene_pos)]
distance1 = abs(chr_3R[0] - search_pos)
distance2 = abs(chr_3R[0] - search_pos)

if distance1 > distance2:
     print(distance2)
else:
     print(distance1)
print(gene_name, abs(chr_3R[mid] - search_pos), iteration)
#print (number_of_iterations)
