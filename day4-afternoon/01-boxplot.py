#!/usr/bin/env python3

"""Usage: ./01-boxplot.py <gene_name> <FPKMS.csv

Box plot all transcripts for a given gene name
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name")
print (df)

goi = df.loc[:,"gene_name"] == gene_name

fpkms = df.drop(columns="gene_name")
#print(fpkms.loc[goi,:])
#print (df.shape)
#print(fpkms.shape)

fig, ax = plt.subplots()
ax.boxplot(fpkms.loc[goi,:].T)
fig.savefig("boxplot.png")
plt.close(fig)