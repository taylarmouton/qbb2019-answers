#first 10,000 reads to a file (40,00 because each read has 4 lines)
head  -n 40000 ../rawdata/SRR072893.fastq > SRR072893.10k.fastq
#generates QC report
fastqc SRR072893.10k.fastq
#maps to reference/index, then converts to SAM file
hisat2 -p 4 -x ../genome/BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam
#Convert .sam to a sorted .bam and index using SAMtools
samtools sort -O bam SRR072893.10k.sam > SRR072893.10k.bam
samtools index -b SRR072893.10k.bam
#Quantitate sorted .bam file using StringTie
#-G <guide_gff>   reference annotation to include in the merging (GTF/GFF3)
  #-o <out_gtf>     output file name for the merged transcripts GTF
                    #(default: stdout)
  #-m <min_len>     minimum input transcript length to include in the merge
                    #(default: 50)
  #-c <min_cov>     minimum input transcript coverage to include in the merge
                    #(default: 0)
  #-F <min_fpkm>    minimum input transcript FPKM to include in the merge
                    #(default: 1.0)
  #-T <min_tpm>     minimum input transcript TPM to include in the merge
                    #(default: 1.0)
  #-f <min_iso>     minimum isoform fraction (default: 0.01)
  #-g <gap_len>     gap between transcripts to merge together (default: 250)
  #-i               keep merged transcripts with retained introns; by default
                   #these are not kept unless there is strong evidence for them
  #-l <label>       name prefix for output transcripts (default: MSTRG)
stringtie SRR072893.10k.bam -G ../genome/BDGP6.Ensembl.81.gtf -e -B -p 4 -o SRR072893.10k.sortedindex.gtf

git add SRR072893.10k.fastq SRR072893.10k.sam SRR072893.10k.bam SRR072893.10k.sortedindex.gtf

