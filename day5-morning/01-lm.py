#!/usr/bin/env python3
"""
./01-lm.py <ctab> (all.csv)

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

goi = pd.DataFrame(df.loc[sys.argv[2]].iloc[1:])
goi.columns = ["FPKM"]

goi["FPKM"] = pd.to_numeric(goi["FPKM"])
goi["sex"], goi["stage"] = goi.index.str.split("_", 1).str
#print(goi)

model = sm.formula.ols(formula= "FPKM ~ sex", data= goi)
#model = sm.formula.ols(formula= "FPKM ~ sex + stage", data= goi)
ols_reults = model.fit()
print(ols_reults.summary())
#print(col_name)
#print(df.loc[sys.argv[2]])