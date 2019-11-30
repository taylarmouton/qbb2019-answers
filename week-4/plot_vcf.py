#!/usr/bin/env python3

"""Plot output.vcf"""

import sys
import matplotlib.pyplot as plt

dp_list = []
qual_value = []
allele_list = []
predicted_dict = {}

#Plotting for Depth Info
for line in open(sys.argv[1]): 
    if line.startswith("#"):
        continue
    column = line.rstrip("\t").split()
    depth_info = column[7]
    dp_info = depth_info.split(";")[7]
    dp_value = dp_info.split("=")[1]
    dp_list.append(dp_value)
    
#Genotype Quality Distribution 
    qual_dist = int(float(column[5]))
    qual_value.append(qual_dist)
#print(qual_value)

#Allele frequency spectrum
    allele_freq = depth_info.split(";")[3]
    allele_val = allele_freq.split("=")[1]
    allele_list.append(allele_val)
#Predicted Effect 
    predict = depth_info.split(";")[41]
    predict_val = predict.split("=")[1]
    predict_only = predict_val.split("|")[1]
    if predict_only in predicted_dict: 
        predicted_dict[predict_only] += 1 
    else:
        predicted_dict[predict_only] = 1 
        
#Graphing the values 
fig,ax = plt.subplots(4)

ax[0].hist(dp_list, bins = 75)
ax[1].hist(qual_value, bins = 1000, range= [0, 5000])
ax[2].hist(allele_list, bins = 100)
plt.bar(range(len(predicted_dict)), list(predicted_dict.values()), align = 'center')
plt.xticks(range(len(predicted_dict)), list(predicted_dict.keys()), rotation = 'vertical', size = 3)


fig.savefig("results_var.png")
plt.close(fig)