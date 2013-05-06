#! /usr/bin/env python
#coding: utf-8

# This Program aim to run bowtie eaisaly
# This version only works for separate paired fastq reads 

# Usage:
# ./bing_bowtie.py ref.fasta R1.fastq R2.fastq out_put_path

# version 0.02
# add print_help()
# index go to index folder
# debug out_put file_names

# version 0.03
# add "-p 3" & "--quiet"

# version 0.04
# add "stderr log" output to a log file

import sys
import os

def print_help():
    print "Usage:\n"
    print "./bing_bowtie.py ref.fasta R1.fastq R2.fastq out_put_path\n"

try:
    assert len(sys.argv) == 5
    ref_fasta = sys.argv[1]
    assert ref_fasta.endswith(".fasta")
    R1_fastq,R2_fastq = sys.argv[2:4]
    assert R1_fastq.endswith(".fastq")
    assert R2_fastq.endswith(".fastq")
    out_put_path = sys.argv[4] if sys.argv[4].endswith("/") else sys.argv[4] + "/"
except:
    print_help()
    sys.exit()

#build bw2 index
basename = ref_fasta[ref_fasta.rfind("/")+1:].replace(".fasta","")
cmd = "mkdir %s"%(out_put_path+"index/")
os.system(cmd)
bt2_index = out_put_path+"index/"+basename
cmd = "bowtie2-build %s %s"%(ref_fasta,bt2_index)

os.system(cmd)
print "#"*100
print "finish build index"
print "#"*100

#run bowtie2
out_put_sam = out_put_path+"Output.sam"
log_file = out_put_path+"Stderr.log"
paramters = "--local -p 3 --un %s --al %s --un-conc %s --al-conc %s"\
        %(out_put_path+"unpaired_unaligned.fastq",\
        out_put_path+"unpaired_aligned.fastq",\
        out_put_path+"paired_unconcordantly.fastq",\
        out_put_path+"paired_concordantly.fastq")

cmd = "bowtie2 %s -x %s -1 %s -2 %s -S %s 2> %s"%\
        (paramters,bt2_index,R1_fastq,R2_fastq,out_put_sam,log_file)
print cmd
os.system(cmd)
