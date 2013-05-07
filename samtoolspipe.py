#! /usr/bin/env python
#coding: utf-8 

#This program could runs samtools pipe on samfile
#This program needs "samtools"
"http://samtools.sourceforge.net/"

import os,sys

def print_usage():
    print "\nUsage:\n"
    print "$./samtoolspipe samfile"

try:
    assert len(sys.argv) == 2
    assert sys.argv[1].endswith(".sam")
except:
    print_usage()

#convert samfile to bam file
sam_file = sys.argv[1]
bam_file = sam_file.replace(".sam",".bam")
cmd = "samtools view -bS %s > %s"%(sam_file,bam_file)
os.system(cmd)
#sort bamfile
sorted_file = sam_file.replace(".sam",".sorted")
cmd = "samtools sort %s %s"%(bam_file,sorted_file)
#build index for bamfile
os.system(cmd)
cmd = "samtools index %s"%(sorted_file)
