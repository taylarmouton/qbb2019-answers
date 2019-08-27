#!/usr/bin/env python3

""""
Compute the average FPKM
"""

import sys
import numpy
import scipy.stats

def read_fpkms_from_t_data(fname):
    all_fpkms = []
    for i, line in enumerate(open(fname)):
        if i == 0:
            continue
        fields = line.rstrip("\n").split("\t")
        fpkm = float(fields[11])
        all_fpkms.append(fpkm)
    return all_fpkms
    
all_fpkms_1 = read_fpkms_from_t_data(sys.argv[1])
all_fpkms_2 = read_fpkms_from_t_data(sys.argv[2])

corr = numpy.corrcoef(all_fpkms_1, all_fpkms_2)

print( "Pearson's R:", corr[0, 1])

rho, pval = scipy.stats.spearmanr(all_fpkms_1, all_fpkms_2)
print("Spearman's rho", rho)

print(scipy.stats.ttest_ind(all_fpkms_1, all_fpkms_2))

print(scipy.stats.ks_2samp(all_fpkms_1, all_fpkms_2))