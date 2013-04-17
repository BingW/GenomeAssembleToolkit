#! /usr/bin/env python
# coding:utf-8
# version 0.02
# this program cut matepair fastqfile's adapters
# first batch cut Junction Adapter
# then batch cut Reads external adapter

__docformat__ = "epytext en"

import os
import sys

def print_help():
    print "Cut MiSeq fastq data adapter"
    print "USAGE\n"
    print "bing_cut_MiSeq_adapter data.fastq\n"
    
Circularized_Duplicate_Junction_Adapter = "CTGTCTCTTATACACATCTAGATGTGTATAAGAGACAG"
Circularized_Single_Junction_Adapter = "CTGTCTCTTATACACATCT"
Circularized_Single_Junction_Adapter_Reverse_Complement = "AGATGTGTATAAGAGACAG"

Read_1_External_Adapter = "GATCGGAAGAGCACACGTCTGAACTCCAGTCAC"
Read_2_External_Adapter = "GATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"

try:
    R = sys.argv[1]
    assert R.endswith(".fastq")
except:
    print_help()

R1 = R.replace(".fastq",".cut_1.fastq")
R2 = R.replace(".fastq",".cut_final.fastq")

cmd = "cutadapt -a %s -a %s -a %s %s > %s"%(Circularized_Duplicate_Junction_Adapter,\
        Circularized_Single_Junction_Adapter,\
        Circularized_Single_Junction_Adapter_Reverse_Complement,R,R1)
os.system(cmd)
cmd = "cutadapt -a %s -a %s %s > %s"%(Read_1_External_Adapter,\
        Read_2_External_Adapter,R1,R2)
os.system(cmd)
cmd = "rm %s "%(R1)
os.system(cmd)

