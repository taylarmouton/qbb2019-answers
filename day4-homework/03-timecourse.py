#!/usr/bin/env python3

"""
Usage: ./02-timecourse.py <t_name> <samples.csv> <FPKMs.>
./03-timecourse.py FBtr0331261 ~/qbb2019/data/samples.csv all.csv
Create a time course of a given transcript for feamles and males 
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Specify transctipt of interest 
t_name = sys.argv[1]

#Load Metadata
samples = pd.read_csv(sys.argv[2])

def sex_sorter(sex):
    soi = samples.loc[:,"sex"] == sex
    stages = samples.loc[soi, "stage"]

    #print(srr_ids)

    #Load FPKMS
    fpkms = pd.read_csv(sys.argv[3], index_col="t_name")

    #Extract Data
    my_data = []
    for stage in stages:
        #print(srr_id)
        my_data.append(fpkms.loc[t_name,sex+ '_' +stage])
    return my_data

#Print my_data
#print(my_data)

male_data = sex_sorter("male")
female_data = sex_sorter("female")
labelz = ["male", "female"]
labelz2 = ["10", "11", "12", "13", "14", "14A", "14B", "14C", "14D"]
#Plot
fig, ax = plt.subplots()
plt.title("Male and Female Data for Sxl Transcripts")
plt.xlabel("Embryonic Stage")
plt.ylabel("mRNA Abundance")
ax.plot(male_data, color="blue")
ax.plot(female_data, color="red")
plt.legend(labels= labelz, loc= "center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()
ax.set_xticklabels(labelz2, rotation='vertical')
ax.set_xticks(np.arange(len(labelz2)))
fig.savefig("timecourse_male_female.png")
plt.close(fig)

#label = "mu=%f;sigma=%f;a=%f" %(mu,sigma,a)