#!/usr/bin/env python2

"""Code for using HiFive to find 3D chromosome architecture, using files from Notes_Code in Week-13 folder"""
import sys
import hifive
import numpy as np

#Load the project file, where r in the first line (line 9 means read the file)
hic = hifive.HiC('Chr10_HIFIVE', 'r')
#Data from our selected region
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
#Selecting only matrix cells with positive expected values using numpy.where to prevent divide-by-zero error
where = np.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
#Log transform
data = np.log(data[:, :, 0] + 0.1)
data -= np.amin(data)


bed_1 = open(sys.argv[1])
bed_2 = open(sys.argv[2])
act_values = {}
rna_values = {}

#Filtering bed files for data of interest based off bin size activity binned
for i, line in enumerate(bed_1):
    if i == 0:
        continue
    col = line.rstrip("\n").split() 
    if int(col[1]) > 5000000 and int(col[1]) < 40000000:
        index = (int(col[1])- 5000000)/5000
        activity = float(col[4])
#Checks dictionary for key, and if not in dictionary, gives default value
        act_values[index] = activity
#Filtering for bed file 2 rna binned
for i, line in enumerate(bed_2):
    if i == 0:
        continue
    col = line.rstrip("\n").split() 
    if int(col[1]) > 5000000 and int(col[1]) < 40000000:
        index = (int(col[1])- 5000000)/5000
        rnaseq = float(col[4])
        # rna_values.setdefault(index, [])
        rna_values[index] = rnaseq
act_rna = {x:act_values[x] for x in act_values  
                              if x in rna_values}
#Multiplying gene x enhancer interaction by enhancers activity in the dictionary
for k in act_values:
    data[:, k] * act_values[k]

data_subset = data[sorted(rna_values.keys()), :][:, sorted(act_values.keys())]

#Make matrix to sum them together all the multiplied values 
pred_exp = list(np.sum(data_subset, axis = 1))
act_exp = [rna_values[k] for k in sorted(rna_values.keys())]

exp_coeff = np.corrcoef(act_exp, pred_exp)[0,1]
print(exp_coeff)