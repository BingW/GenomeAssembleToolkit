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

# version 0.14 
# add "-p" for paired reads bowtie
# add "-s" for unpaired reads bowtie
# more structured

import sys
import os

def print_help():
    print "Usage:\n"
    print "for paired reads:"
    print "./bing_bowtie.py ref.fasta R1.fastq R2.fastq out_put_path\n"
    print "or "
    print "./bing_bowtie.py -p ref.fasta R1.fastq R2.fastq out_put_path\n"
    print "for single reads:"
    print "./bing_bowtie.py -s ref.fasta reads.fastq out_put_path\n"

def build_bw2index(ref_fsa,out_path):
    #build bw2 index
    basename = ref_fsa[ref_fsa.rfind("/")+1:].replace(".fasta","")
    cmd = "mkdir %s"%(out_path+"index/")
    os.system(cmd)
    bt2_index = out_path+"index/"+basename
    cmd = "bowtie2-build %s %s"%(ref_fsa,bt2_index)
    os.system(cmd)
    print "#"*100
    print "finish build index"
    print "#"*100
    return bt2_index

def run_bowtie_paired(R1,R2,index,out_path):
    #run bowtie2
    out_put_sam = out_path+"Output.sam"
    log_file = out_path+"Stderr.log"
    paramters = "--local -p 3 --un %s --al %s --un-conc %s --al-conc %s"\
            %(out_path+"unpaired_unaligned.fastq",\
            out_path+"unpaired_aligned.fastq",\
            out_path+"paired_unconcordantly.fastq",\
            out_path+"paired_concordantly.fastq")

    cmd = "bowtie2 %s -x %s -1 %s -2 %s -S %s 2> %s"%\
            (paramters,index,R1,R2,out_put_sam,log_file)
    print cmd
    os.system(cmd)

def run_bowtie_singl(R,index,out_path):
    out_put_sam = out_path+"Output.sam"
    log_file = out_path+"Stderr.log"
    paramters = "--local -p 3"
    cmd = "bowtie2 %s -x %s -U %s -S %s 2> %s"%\
            (paramters,index,R,out_put_sam,log_file)
    print cmd
    os.system(cmd)

def check_paramters(argv):
    if "-p" in argv:
        assert len(argv) == 6
        assert argv[2].endswith(".fasta")
        assert argv[3].endswith(".fastq")
        assert argv[4].endswith(".fsatq")
    elif "-s" in argv:
        assert len(argv) == 5
        assert argv[2].endswith(".fasta")
        assert argv[3].endswith(".fastq")
    else:
        assert len(argv) == 5
        assert argv[1].endswith(".fasta")
        assert argv[2].endswith(".fastq")
        assert argv[3].endswith(".fsatq")

def mian(argv):
    check_paramters(argv)

    if "-p" in argv:
        ref_fasta = argv[2]
        R1_fastq,R2_fastq = argv[3:5]
        out_put_path = argv[5] if argv[5].endswith("/") else argv[4] + "/"
        bt2_index = build_bw2index(ref_fasta,out_put_path)
        run_bowtie_paired(R1_fastq,R2_fastq,bt2_index,out_put_path)

    elif "-s" in argv:
        ref_fasta = argv[2]
        R_fastq = argv[3]
        out_put_path = argv[4] if argv[4].endswith("/") else argv[4] + "/"
        bt2_index = build_bw2index(ref_fasta,out_put_path)
        run_bowtie_singl(R_fastq,bt2_index,out_put_path)

    else:
        ref_fasta = argv[1]
        R1_fastq,R2_fastq = argv[2:4]
        out_put_path = argv[4] if argv[4].endswith("/") else argv[4] + "/"
        bt2_index = build_bw2index(ref_fasta,out_put_path)
        run_bowtie_paired(R1_fastq,R2_fastq,bt2_index,out_put_path)

if __name__ == "__main__":
    main(sys.argv)
 


