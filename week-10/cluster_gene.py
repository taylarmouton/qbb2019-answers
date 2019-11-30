#!/usr/bin/env python3

"""From .txt file to make an array of the data for numpy to generate heat map and compare gene expression"""

import sys
import numpy as np
import matplotlib.pylab as plt 
import scipy
import seaborn as sns  
import pandas as pd 
from scipy.cluster.hierarchy import dendrogram, linkage

datafile = open(sys.argv[1])

data = pd.read_csv(datafile, sep = "\t", header = 0, index_col = "gene")
#print(data)

linkage_1 = scipy.cluster.hierarchy.linkage(data, method='average')
leaf_1 = scipy.cluster.hierarchy.leaves_list(linkage_1)
#print(leaf_1)
#genes = data["gene"]
#print(genes)
new_data = data.iloc(leaf_1)
print(new_data)
"""Making a list/index in data frame"""
#genes = data["gene"].values
#print(genes)





"""Plotting unsorted heatmap"""
# gene_array = np.random.rand(10, 12)
#ax = sns.heatmap(data, linewidth=0.5)

# sns.heatmap(data)
# plt.show()
#
# Z = linkage(X, 'ward')
