#!/usr/bin/env python3

"""Usage: ./01-hist.py <ctab> <mu> <sigma> <a>

Where mu is standard deviation and and sigma is your mean. a is your skew parameter. User sets these values.

Plot FPKm
"""


import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = fields = line.rstrip("\n").split("\t")
    if float(fields[11])> 0:
        fpkms.append(float(fields[11]))
#print(len(fpkms))

my_data = np.log2(fpkms)
mu = float(sys.argv[2])
sigma = float(sys.argv[3])
a = float(sys.argv[4])

x = np.linspace(-15, 15, 100)
y1 = stats.skewnorm.pdf(x, a, loc = mu, scale = sigma) 
y2 = stats.norm.pdf(x, mu, sigma) 
#print (x)
#print(type(x)) 

fig, ax = plt.subplots()
ax.hist(my_data, bins=100, density = True)
plt.title("FPKM Data: Abundance of RNA")
plt.xlabel("FPKM Value")
plt.ylabel("Percent of Frequency")
ax.plot(x, y1, color="pink" , label = "mu=%f;sigma=%f;a=%f" %(mu,sigma,a))
ax.plot(x, y2, color="orange", label = "mu=%f;sigma=%f" %(mu,sigma))
ax.legend()
fig.savefig("fpkms_with_labels.png")
plt.close(fig)