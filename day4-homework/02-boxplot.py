#!/usr/bin/env python3

"""Usage: ./02-boxplot.py <gene_name> <FPKMS.csv>

Box plot all transcripts for a given gene name based off of sex


"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name")
print (df)

goi = df.loc[:,"gene_name"] == gene_name

fpkms = df.drop(columns="gene_name")
filtered_fpkms = fpkms.loc[goi,:]

male_ids = [y for y in list(filtered_fpkms) if y.startswith('male')]
male_transcripts = np.log2(filtered_fpkms[male_ids] + 0.001)
female_ids = [x for x in list(filtered_fpkms) if x.startswith('female')]
female_transcripts = np.log2(filtered_fpkms[female_ids] + 0.001)

male_x_axes = [y[5:] for y in male_ids]
female_x_axes = [x[7:] for x in female_ids]
#print(fpkms.loc[goi,:])
#print (df.shape)
#print(fpkms.shape)

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.boxplot(male_transcripts.T)
ax1.set_xlabel("Embryo Stage in Days")
ax1.set_ylabel("Transcript Count of Sxl")
ax1.set_xticklabels(male_x_axes, fontsize=7)
ax2.boxplot(female_transcripts.T)
ax2.set_xlabel("Embryo Stage in Days")
ax2.set_ylabel("Transcript Count of Sxl")
ax2.set_xticklabels(female_x_axes, fontsize=7)
plt.title("Sxl Data: Males and Females During Embryo Stage")
plt.tight_layout()
fig.savefig("boxplot_fem_male.png")
plt.close(fig)