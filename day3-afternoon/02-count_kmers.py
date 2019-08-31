#!/usr/bin/env python3

"""
Count all kmers in FASTA file
"""

from fasta import FASTAReader
import sys

reader = FASTAReader(sys.stdin)
k = int(sys.argv[1])

kmers = {}

for ident, sequence in reader:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1
            
for kmer, count in sorted(kmers.items(),
                           key=lambda t: t[1]):
    print(kmer, count, sep="\t")