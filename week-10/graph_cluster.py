#!/usr/bin/env python3

"""From .txt file to make an array of the data for numpy to generate heat map and compare gene expression
    Sys.argv[2] is the Adcy6 gene"""

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
#print(new_data)
"""Making a list/index in data frame"""
#genes = data["gene"].values
#print(genes)
transposed_new_data = new_data.transpose()
​
linkage_2 = linkage(transposed_new_data, method = 'average')
leaf_2 = scipy.cluster.hierarchy.leaves_list(linkage_2)
finish_last_data = transposed_new_data.iloc[leaf_2]
​
final_transposed = finish_last_data.transpose()

#Z = linkage(data, 'single')
fig = plt.figure(figsize=(5, 3))
​
plt.xlabel('Cell Types')
​
plt.title('Dendrogram')
plt.grid(True)


label_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
labels = np.array(label_list)
sort_label = labels[leaves_list_2]
ax1 = dendrogram(linkage_2, labels = sort_label)
plt.show()
​
#k means clustering
cfu = data["CFU"].values
poly = data["poly"].values
​

# from scipy.cluster.vq import vq, kmeans, whiten
# test = kmeans(cfu,poly)
from sklearn.cluster import KMeans
from pandas import DataFrame
​
Data = {'x':cfu,
        'y': poly
       }
  
df = DataFrame(Data,columns=['x','y'])
#print (df)
​
kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_
#print(centroids)
​
plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.xlabel("CFU")
plt.ylabel("poly")
plt.title('K-means')
plt.show()
​
​
#kmeans = KMeans(n_clusters=5).fit(data)
cluster_map = pd.DataFrame()
cluster_map['data_index'] = df.index.values
cluster_map['cluster'] = kmeans.labels_
cluster_map[cluster_map.cluster == 5]
​
print(cluster_map)
​

rom scipy import stats
​
diff_exp_high = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) >= 2
diff_exp_low = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) <= 0.5
​
diff_exp_genes = data[diff_exp_high | diff_exp_low]
#print(diff_exp_genes)
for gene_name, row in diff_exp_genes.iterrows():
    sample1 = [row['CFU'], row['unk']]
    sample2 = [row['poly'], row['int']]
    # print(gene_name, stats.ttest_rel(sample1, sample2).pvalue)
    pval = stats.ttest_rel(sample1, sample2).pvalue
    if pval <= 0.05:
        print(gene_name, pval)
​
​
​
labels = list(kmeans.labels_)
genes = list(data.index.values)
​
goi_index = genes.index(sys.argv[2])
goi_cluster = labels[goi_index]
​
related_genes = []
for i, gene in enumerate(genes):
    if labels[i] == goi_cluster:
        related_genes.append(gene)
​
print(related_genes)
​
with open('list_of_genes.txt', 'w') as f:
    for item in related_genes:
        f.write("%s," % item)