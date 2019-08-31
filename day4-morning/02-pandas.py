#!/usr/bin/env python3

"""Usage: ./02-pandas.py <ctab>

Compare num_exons vs length... using pandas
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

#exons = []
#lengths = []

ctab = pd.read_csv(sys.argv[1], sep="\t")
#print(type(ctab))
#print(ctab)

exons = ctab.loc[:, "num_exons"]
lengths = ctab.loc[:, "length"]
print(ctab.describe())
#for i, line in enumerate(open(sys.argv[1])):  
#    if i == 0:
#        continue
#    fields = line.rstrip("\n").split("\t")
#    exons.append(int(fields[6]))
#    lengths.append((int(fields[7])))
    
fig, ax = plt.subplots()
ax.scatter(x=exons, y=lengths)
#Passes each point through the respective x and y 
ax.plot( [0, 40], [0, 20000], color="red")
fig.savefig("exon-v-length.png")
plt.close(fig)