#!/usr/bin/env python3

"""Input is fimo.tsv, which is located in the fimo_output_1 folder from meme_results in week 9"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import seaborn as sns

#argv1=fimo.tsv
f = open(sys.argv[1])
locations = []
for line in f:
   if line.startswith("motif_id"):
       continue
   col = line.rstrip("\n").split()
   if col != []:
       locations.append(int(col[3]))
fig, ax = plt.subplots()
ax = sns.distplot(a=locations, bins = 10).set_title('Density plot of location of motif matches')


plt.xlabel('Relative Sequence Location')
plt.ylabel('Density')



fig.savefig("densityplot.png", dpi=1200)
plt.close(fig)

plt.show()