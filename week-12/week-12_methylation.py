#!/usr/bin/env python3

"""Finding difference in sites of methylation using ES_f_mC_1 and EpiSC_mC_1 the bismark version with bedgraph"""

import sys
import os
import numpy as np

data_1 = []
data_2 = []
upmeth_1 = []
upmeth_2 = []

for line in open(sys.argv[1]):
    column = line.rstrip("\t").split()
    pos1 = column[1]
    meth1 = float(column[3])
    if meth1 >= 50: 
        data_1.append(meth1)
for line in open(sys.argv[2]):
    column = line.rstrip("\t").split()
    pos2 = column[1]
    meth2 = float(column[3])
    if meth2 >= 50: 
        data_2.append(meth2)
for site in data_1: 
    if site not in data_2:
        upmeth_1.append(site)
for site in data_2: 
    if site not in data_1:
        upmeth_2.append(site)
        
 """make output into a file"""              

