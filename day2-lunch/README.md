#first 10,000 reads to a file (40,00 because each read has 4 lines)
head  -n 40000 ../rawdata/SRR072893.fastq > SRR072893.10k.fastq
#generates QC report
fastqc SRR072893.10k.fastq
#maps to reference/index, then converts to SAM file
hisat2 -p 4 -x ../genome/BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam
#Convert .sam to a sorted .bam and index using SAMtools
samtools sort -O bam SRR072893.10k.sam > SRR072893.10k.bam (converts output path to a file which we created) SRR072893.10k.bam SRR072893.10k.bam.bai (index and then just write in new file that we want)

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

#Question 3
#slow method
grep "^SRR072893" SRR072893.10k.sam | cut -f 3| sort | uniq -c > SRR072893.txt
cut -f 3 SRR072893.sam | sort | uniq -c
1 211000022278750 2 211000022278876 1 211000022278877 1 211000022278878 5 211000022278879 1 211000022278881 2 211000022279055 1 211000022279100 2 211000022279109 1 211000022279132 2 211000022279222 3 211000022279343 1 211000022279420 1 211000022279446 1 211000022279540 3 211000022279676 1 211000022279708 1 211000022279810 2 211000022280043 2 211000022280304 1 211000022280508 1 211000022280645 5724 2L 6821 2R 6117 3L 7990 3R 444 4 1 Unmapped_Scaffold_58 5848 X 32 Y 73 dmel_mitochondrion_genome 35 rDNA
(sort sam file (a readable format), which is the result of converting the hisat2 files which have a header and aligment section. bam file is no good b/c it's a compressed binary (file unreadale))

#fast use the sorted file from before

#Question 4
samtools view SRR072893.sam | awk '{print NF}' | sort SRR072893.sam | uniq -c > SRR072893.columns
tail -n 10  SRR072893.columns > SRR072893.columns.last