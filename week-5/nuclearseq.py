#!/usr/bin/env python3

import sys
from fasta import FASTAReader
import numpy as np
import matplotlib.pyplot as plt



f = open(sys.argv[1])
f2 = open(sys.argv[2])

reader = FASTAReader(f)
reader2 = FASTAReader(f2)

count = 0
protein_seq = {}
for ident, seq in reader:
   count += 1
   ident = count
   protein_seq[ident] = seq

count2 = 0
nt_seq = {}
for ident, seq in reader2:
   count2 += 1
   ident = count2
   nt_seq[ident] = seq

new_seq = {}
for ident in protein_seq:
   pseq = protein_seq[ident]
   nseq = nt_seq[ident]
   newline = ""
   nuc_pos = 0
   for character in pseq:
       if character == "-":
           newline += "---"
       else:
           newline += nseq[nuc_pos:nuc_pos+3]
           nuc_pos += 3
   new_seq[ident] = newline

table = {
       'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
       'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
       'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
       'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
       'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
       'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
       'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
       'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
       'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
       'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
       'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
       'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
       'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
       'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
       'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
       'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
   }

z_score = {}
d_score = []
for i in range(0,len(new_seq[1]), 3):
   q_codon = new_seq[1][i:i+3]
   ds_count = 0
   dn_count= 0
   for ident in new_seq:
       seq_codon = new_seq[ident][i:i+3]
       if q_codon != seq_codon:
           if q_codon == '---' or seq_codon == '---':
               continue
           # print(q_codon)
           # print(seq_codon)
           if q_codon not in table or seq_codon not in table:
               continue
           if table[q_codon] == table[seq_codon]:
               ds_count += 1
           else:
               dn_count += 1

   d = dn_count - ds_count
   d_score.append(d)
std = np.std(d_score)
print(d_score)
for i,d in enumerate(d_score):
   z_score[i] = d/std



x = []
y = []
for key in z_score:
   x.append(key)
   value = z_score[key]
   y.append(value)



fig, ax = plt.subplots()
ax.scatter(x, y)
plt.xlabel("Sequence Idenitites")
plt.ylabel("Z Scores")
plt.title ("Z Scores")
fig.savefig("zscores.png")
plt.close(fig)