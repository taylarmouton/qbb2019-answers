#!/usr/bin/env python3

"""Usage: ./00-scatter.py <ctab1> <ctab2>

Compare FPKM1 vs FPKM2
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fpkms1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

fpkms2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkmss1 = np.log2(ctab1.loc[:,"FPKM"] + 0.01)
print(fpkmss1)
fpkmss2 = np.log2(ctab2.loc[:, "FPKM"] + 0.01)
print(fpkmss2)

m, b = np.polyfit(fpkmss1, fpkmss2, 1)
x = [fpkmss1.min(), fpkmss2.max()]


fig, ax = plt.subplots()
ax.scatter(x=fpkmss1, y=fpkmss2, s=3, alpha=0.5)
#Passes each point through the respective x and y 
ax.plot(x, [(m*x1+b) for x1 in x], color="green", label= "y = %sx + %s" %(str(m)[:5], str(b)[:5]))
ax.legend()
plt.title("Exon Vs. Length")
plt.xlabel("FPKMS 1")
plt.ylabel("FPKMS 2")
fig.savefig("FPKM1-v-FPKM2.png")
plt.close(fig)