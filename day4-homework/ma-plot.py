#!/usr/bin/env python3

"""
Usage: ./ma-plot.py <ctab1> <ctab2>
./03-timecourse.py FBtr0331261 ~/qbb2019/data/samples.csv all.csv
Create a time course of a given transcript for feamles and males

../results/stringtie/SRR72...
../results/stringtie SRR072916 SRR072915 SRR072914 
"""
#you just have to import two ctab files

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

#fpkm = {"sample1" : [1, 2, 3]
#        "sample2" : [4, 5, 6]}

fpkm = {name1 : ctab1.loc[:,"FPKM"],
        name2 : ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm)
df += 1 #because log(0) doesn't work

#print(df)
#print(type(df))

r =df.loc[:,name2]
g =df.loc[:,name1]
m = np.log2(r/g)
a = .5 * np.log2(r*g)

fig, ax = plt.subplots()
ax.scatter( x=a, y=m, s = 3, alpha = .3)
ax.set_title("SRR072893 and SRR072894")
ax.set_xlabel("m")
ax.set_ylabel("a")
fig.savefig("ma-plot.png")
plt.close(fig)

