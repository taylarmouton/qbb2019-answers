#!/usr/bin/env python3
"""
./02-scree.py <ctab> (all.csv) <t_name>
 PC Analysis 
"""
#FBtr0302347
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = df = pd.read_csv(sys.argv[1], index_col="t_name")
df = df.drop(columns = "gene_name")

n, p = df.shape

#print(df.shape)

fit = PCA().fit(df.T)

fig, ax = plt.subplots()
ax.bar(range(p), fit.explained_variance_ratio_)
fig.savefig("scree.png")
plt.close(fig)
#print(fit.explained_variance_ratio_)