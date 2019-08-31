#!/usr/bin/env python3

"""
Usage: ./02-timecourse.py <t_name> <samples.csv> <FPKMs.>

Create a time course of a given transcript for feamles
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt


#Specify transctipt of interest 
t_name = sys.argv[1]

#Load Metadata
samples = pd.read_csv(sys.argv[2])
soi = samples.loc[:,"sex"] == "female"
srr_ids = samples.loc[soi, "sample"]

#print(srr_ids)

#Load FPKMS
fpkms = pd.read_csv(sys.argv[3], index_col="t_name")

#Extract Data
my_data = []
for srr_id in srr_ids:
    #print(srr_id)
    my_data.append(fpkms.loc[t_name,srr_id])

#Print my_data
#print(my_data)

#Plot
fig, ax = plt.subplots()
ax.plot(my_data)
fig.savefig("timecourse.png")
plt.close(fig)

