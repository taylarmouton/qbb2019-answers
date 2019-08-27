#!/bin/bash

GENOME=../genome/BDGP6
ANNOTATION=../genome/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq
  hisat2 -p $THREADS -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort -O bam $SAMPLE.sam > $SAMPLE.bam
  samtools index -b $SAMPLE.bam
  stringtie $SAMPLE.bam -G $ANNOTATION -e -B -p $THREADS -o $SAMPLE.gtf
done