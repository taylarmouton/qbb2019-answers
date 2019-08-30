#!/usr/bin/env python3
"""
Usage for multiple linear regression comparing H3K4me1_compare, H3K4me3_compare, H3K9me3_compare

./01-mlr.py ../results/stringtie/...
SRR072893

"""
#FBtr0302347
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy 

ctab = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
hist1 = pd.read_csv(sys.argv[2], sep="\t", index_col= 0, header= None)
hist2 = pd.read_csv(sys.argv[3], sep="\t", index_col= 0, header= None)
hist3 = pd.read_csv(sys.argv[4], sep="\t", index_col= 0, header= None)

histone_mods = {"FPKM": ctab.loc[:, "FPKM"],
                "H3K4me1": hist1.iloc[:, -1],
                "H3K4me3": hist2.iloc[:, -1],
                "H3K9me3": hist3.iloc[:, -1],}

#print Data Frame
histone_df = pd.DataFrame(histone_mods)
#print(histone_df)

model = sm.formula.ols(formula= "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data= histone_df)
ols_results = model.fit()
#print(ols_reults.summary())
#print(ols_results.resid)
#histmod = {"t_name": ctab.loc[:, "FPKM"]}
#for i, line in enumerate(open(sys.argv[2])):

#Plotting in Histogram
fig, ax = plt.subplots()
ax.hist(ols_results.resid, bins=1000, range=(-100, 100))
ax.set_xlim(-100, 100)
plt.xlabel("Residual")
plt.ylabel("Frequency")
plt.title("FPKM and Histone Mod Residual")
fig.savefig("residuals.png")
plt.close(fig)
    
    
