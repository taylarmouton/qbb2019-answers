#!/usr/bin/env python3

"""
Match all kmers in FASTA file to droYak2
"""
#importing FASTAReader function 
from fasta import FASTAReader
import sys

#Setting variables 
target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

#Making dictionary for kmers of target to be stored
kmer_of_target = {}

#For arguement for storing the target 
for ident, sequence in target:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k + 1):
        kmertarget = sequence[i:i+k]
        if kmertarget not in kmer_of_target:
            kmer_of_target[kmertarget] = [(ident, i)]
        else:
            kmer_of_target[kmertarget].append((ident, i))

#For statement to check query kmer to stored target kmer
for ident2, sequence in query:
    sequence = sequence.upper()
    for j in range(0, len(sequence) - k + 1):
        kmerquery = sequence[j:j+k]
        if kmerquery not in kmer_of_target:
            continue
        else:
            list_of_dupes = kmer_of_target[kmerquery]
            for ident, i in list_of_dupes:
                print(ident, i, j, kmerquery)
                   