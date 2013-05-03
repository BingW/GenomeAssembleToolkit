#! /usr/bin/env python
#coding: utf-8

# This Program aim to run bowtie eaisaly
# This version only works for separate paired fastq reads 
# Usage:
# bowtie2 ref.fasta R1.fastq R2.fastq out_put_path

import sys
import os

assert len(sys.argv) == 5
ref_fasta = sys.argv[1]
assert ref_fasta.endswith(".fasta")
R1_fastq,R2_fastq = sys.argv[2:4]
assert R1_fastq.endswith(".fastq")
assert R2_fastq.endswith(".fastq")
out_put_path = sys.argv[4] if sys.argv[4].endswith("/") else sys.argv[4] + "/"

#build bw2 index
basename = ref_fasta[ref_fasta.rfind("/")+1:].replace(".fasta","")
bt2_index = out_put_path+basename
cmd = "bowtie2-build %s %s"%(ref_fasta,bt2_index)
os.system(cmd)

#run bowtie2
out_put_sam = out_put_path+"Output.sam"
paramters = "--local --un %s --al %s --un-conc %s --al-conc %s"\
        %(out_put_path,out_put_path,out_put_path,out_put_path)
cmd = "bowtie2 -x %s -1 %s -2 %s %s -S %s"%(bt2_index,R1_fastq,R2_fastq,paramters,out_put_sam)
os.system(cmd)
