#!/usr/bin/env python3

"""Usage: 

././00-transcription-for-SRR.py <t_data.ctab> 

"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


ctab = pd.read_csv(sys.argv[1], sep="\t")
all_start_end_values = ctab.loc[:,["chr", "t_name", "strand", "start", "end"]]
#all_start_end_values["promoter start"] = ""

#Labels
print("Chr" + "\t" + "t_name" + "\t" + "promoter start" + "\t" + "promoter end")
#Iterating throws in dataframe
for index, row in all_start_end_values.iterrows():
   if row.loc["strand"] == "+":
       promoterStart = int(row.loc["start"])
       promoter_start_plus_500 = promoterStart + 500
       promoter_start_minus_500 = promoterStart - 500
       print(str(row.loc["chr"]) + "\t" + str(row.loc["t_name"]) + "\t" + str(promoter_start_minus_500) + "\t" + str( promoter_start_plus_500))
   elif row.loc["strand"] == "-":
       promoterStart = int(row.loc["end"])
       promoter_start_plus_500 = promoterStart + 500
       promoter_start_minus_500 = promoterStart - 500
       print(str(row.loc["chr"]) + "\t" + str(row.loc["t_name"]) + "\t" + str(promoter_start_minus_500) + "\t" + str( promoter_start_plus_500))