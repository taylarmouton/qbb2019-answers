#!/usr/bin/env python3

import sys
#Code to use for Identifier Mapping

#defining dictionary
d_flybase = {}

#opening out file from Exercise 1
for line in open("day2-homework.out"):
    columns = line.rstrip("\n").split("\t")
    #naming variables for lists from output file
    list_genes_flybase = columns[0].strip()
    list_genes_uniprot = columns[1].strip()
    d_flybase[list_genes_flybase]= list_genes_uniprot
for i, line in enumerate(open("../results/stringtie/SRR072893/t_data.ctab")):
    if i == 0:
        continue
    new_columns = line.rstrip("\n").split("\t")
    list_genes_ctab = new_columns[8]
    if list_genes_ctab in d_flybase:
        d_flybase[list_genes_ctab]= list_genes_uniprot
        print(line.strip("\n"), d_flybase[list_genes_ctab])
    elif list_genes_ctab not in d_flybase and sys.argv[1] == "nothing":
        continue
    elif list_genes_ctab not in d_flybase and sys.argv[1] == "default":
        print(line.strip("\n"), "N/A")
        


