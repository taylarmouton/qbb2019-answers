#!/usr/bin/env python3
"""
./00-dge-by-sex.py <ctab> (all.csv)

"""
#FBtr0302347
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy 

df = pd.read_csv(sys.argv[1], index_col="t_name")
#col_name = df.columns
col_name = df.columns.values.tolist()

def sex_dge(transcript_id):
    goi = pd.DataFrame(df.loc[transcript_id].iloc[1:])
    goi.columns = ["FPKM"]

    goi["FPKM"] = pd.to_numeric(goi["FPKM"])
    goi["sex"], goi["stage"] = goi.index.str.split("_", 1).str
    #print(goi)
    
    goi["stage"].replace("14A", "14", inplace= True)
    goi["stage"].replace("14B", "15", inplace= True)
    goi["stage"].replace("14C", "16", inplace= True)
    goi["stage"].replace("14D", "17", inplace= True)
    
    goi["stage"] = pd.to_numeric(goi["stage"])
    
    goi["logFPKM"] = np.log(goi["FPKM"] + 1)

    model = sm.formula.ols(formula= "FPKM ~ sex + stage", data= goi)
    #model = sm.formula.ols(formula= "FPKM ~ sex + stage", data= goi)
    ols_reults = model.fit()
#    print(result_df)
#    print(ols_reults.summary())
    return(transcript_id, ols_reults.pvalues[1], ols_reults.pvalues[2])
#    print(sex_dge("FBtr0302347"))
#print(col_name)
#print(df.loc[sys.argv[2]])

#sex_dge("FBtr0302347")

#hi_exp_gene = ((df == 0).sum(axis=1) <= 3) #less than or equal to three zeros
hi_exp_gene = ((df == 0).sum(axis=1) == 0) #for no zeros
hi_df = df.loc[hi_exp_gene, :]
hi_exp_genes_list = hi_df.index.values.tolist()
#print(hi_df.shape)
results = []
for transcript in hi_exp_genes_list:
    results.append(sex_dge(transcript))

results_df = pd.DataFrame(results, columns= ["t_name", "p_val_sex", "p_val_stage"]).sort_values(by= "p_val_stage")
print(results_df)

fig, ax = plt.subplots()
hist = ax.hist(results_df.loc[:, "p_val_stage"])
fig.savefig("pvalhist.png") #GIVES MISSPECIFIED GRAPH; if no assoc. would see a more noramlly distributed graph--> errror dist. issue
plt.close(fig)

#print(results)
#print(hi_exp_gene)