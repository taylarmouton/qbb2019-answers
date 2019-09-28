#!/usr/bin/env python3

"""Running PCA on data and plotting"""

import sys
import matplotlib.pyplot as plt

 #plink.eigenvec file

pca1= []
pca2= []

for line in open(sys.argv[1]):
    col = line.split(" ")
    comp1= float(col[2])
    comp2= float(col[3])
    pca1.append(comp1)
    pca2.append(comp2)
#print(pca1) 

#Plotting PCA
fig, ax = plt.subplots()
ax.scatter(pca1, pca2)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("PCA for Variants")
fig.savefig("pca.png")
plt.close() 

#Plotting Allele Frequency 

fig, ax = plt.subplots()
ax.hist(my_data, bins=100, density = True)
ax.plot(x, y)
fig.savefig("fpkms.png")
plt.close(fig)