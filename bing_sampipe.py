#! /usr/bin/env python
#coding: utf-8 

#This program could runs samtools pipe on samfile
#This program needs "samtools"
"http://samtools.sourceforge.net/"
#version 0.01
#1: sam -> bam
#2: bam -> sort by pos bam
#3: bam -> sort by name bam
#4: build index for bams

import os,sys

def print_usage():
    print "\nUsage:\n"
    print "$./samtoolspipe samfile\n"
    print "This program will convert samfile to bamfile and sort it by name and by position, then build index for them"

def check_argv(argv):
    try:
        assert len(argv) == 2
        assert argv[1].endswith(".sam")
    except:
        print_usage()
        sys.exit()

def main(argv):
    check_argv(argv)
    sam_file = argv[1]
    bam_file = sam_file.replace(".sam",".bam")
    cmd = "samtools view -bS %s > %s"%(sam_file,bam_file)
    print cmd
    print "Step:1 convert samfile to bamfile"
    print "#"*80
    os.system(cmd)


    sorted_file = sam_file.replace(".sam",".sorted_by_pos")
    cmd = "samtools sort %s %s"%(bam_file,sorted_file)
    print cmd
    print "Step:2 sort bamfile by position"
    print "#"*80
    os.system(cmd)


    cmd = "samtools index %s"%(sorted_file+".bam")
    print cmd
    print "Step:3 build index for sorted by position bamfile"
    print "#"*80
    os.system(cmd)


    sorted_file = sam_file.replace(".sam",".sorted_by_name")
    cmd = "samtools sort %s %s"%(bam_file,sorted_file)
    print cmd
    print "Step:4 sort bamfile by name"
    print "#"*80
    os.system(cmd) 


    cmd = "samtools index %s"%(sorted_file+".bam")
    print cmd
    print "Step:5 build index for sorted by name bamfile"
    print "#"*80
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv)
