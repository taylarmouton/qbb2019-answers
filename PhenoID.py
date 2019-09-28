#!/usr/bin/env python3

"""Adding ID markers to Pheno File (individual (_#) and family (A0#))"""

import sys

fam_id = []
indiv_id = []
for i,line in enumerate(open(sys.argv[1])):
    if i == 0:
        print('\t'.join(["FID","IID"] + [line.strip()]))
    else:
        column = line.rstrip("\t").split()
        value = column[0]
        family = value.split("_")[0]
        indiv = value.split("_")[1]
        print('\t'.join([family,indiv] + column[1:]))
    # fam_id.append(family)
    # indiv_id.append(indiv)
# print(fam_id)
# print(indiv_id)

