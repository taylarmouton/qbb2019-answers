#!/usr/bin/env python3

"""Plotting hist of AF"""

import sys
import matplotlib.pyplot as plt


#Parsing AF Data    
freq = []

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue 
    column = line.rstrip("\t").split()
    af = column[7]
    af_value = af.split("=")[1]
    if "," in af_value: 
        af_value= float(af_value.split(",")[0])
    else:
        af_value = float(af_value)
    freq.append(af_value)
#print(freq)

#Plotting Histogram 
fig, ax = plt.subplots()
ax.hist(freq, bins=1050, density = True)
ax.set_xlabel("Allele")
ax.set_ylabel("Frequency")
ax.set_title("Allele Frequency Spectrum")
#ax.plot(x, y)
fig.savefig("af.png")
plt.close(fig)