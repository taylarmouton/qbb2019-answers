#!/usr/bin/env python3

"""
Parse and print all records from a FASTA file
"""

import sys

class FASTAReader(object):
    
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False
    
    def next(self):
        
        if self.eof:
            return None, None
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
        #If reach this point, ident is set correctly
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append(line.strip())
        sequence = "".join(sequences)
        return ident, sequence 



#What I wasnt to work:

reader = FASTAReader(sys.stdin)

while True:
    ident, sequence = reader.next()
    if ident is None:
        break
    print(ident, sequence)