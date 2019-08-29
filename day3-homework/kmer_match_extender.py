#!/usr/bin/env python3

"""
Match all kmers in FASTA file to droYak2 and extend the genes for alignment 
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
list_ =[]

#For statement to check query kmer to stored target kmer

for ident2, sequence in query:
    ignore = set()
    sequence = sequence.upper()
    j = 0 
    for j in range(0, len(sequence) - k + 1):
        kmerquery = sequence[j:j+k]
        if kmerquery not in kmer_of_target:
            continue
        else:
            list_of_dupes = kmer_of_target[kmerquery]
            for ident, i in list_of_dupes:
                if (ident,i) in ignore:
                    continue
                x = j + 1
                last_start = i
                match_len = k
                end = i+k-1
                end2 = x+k-1
                seq = kmerquery
                while x < len(sequence) - k  + 1:
                    next_kmer = sequence[x:x+k]
                    if next_kmer in kmer_of_target:
                        shifted = False
                        for next_ident, next_i in kmer_of_target[next_kmer]:
                            #Is our next query in the same target sequence, and is it offset by 1?
                            if ident == next_ident and last_start + 1 == next_i:
                                match_len += 1
                                end += 1
                                end2 += 1
                                last_start += 1
                                shifted = True
                                seq = seq + next_kmer[-1]
                                ignore.add((next_ident,next_i))
                                break
                        if not shifted: 
                            break
                    else:
                        break
                    x += 1
                # print(match_len)
                list_.append((ident, i, j, match_len,seq))


for ident,i,j,match_len,seq in sorted(list_, key= lambda t : t[3],reverse = True):
    print(match_len,seq)
#                print(ident, i, j, kmerquery)

