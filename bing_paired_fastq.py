#! /usr/bin/env python 
#coding:utf-8
#this program can do combine,separate,devide fastq file(s)

#version 0.1
#bing_paired_fastq --separate
#bing_paired_fastq --combine
#bing_paired_fastq --devide

#version 0.11
#structed
#bing_paired_fastq --fromlist

#version 0.12
#data structure improved for bing_paired_fastq
#now it's much faster

import os,sys
import math

def print_usage():
    print "\nUsage:\n"
    print "To separate an intergrated paired fastq file into Reads1.fastq and Reads2.fastq."
    print "$./bing_paired_fastq --separate fastq_to_be_separate\n"
    print "To combine separated Reads_1 and Reads_2 into one intergrated fastq file"
    print "$./bing_paired_fastq --combine Reads_1 Reads_2 out_put_combined_fastq\n"
    print "To devide an intergrated paired fastq file into n parts"
    print "$./bing_paired_fastq --devide fastq_to_be_devide n\n"
    print "To get subset of fastqfile from a list"
    print "$./bing_paired_fastq --fromlist fastq_file list_file > outfile\n"

def veriry_arguments(argv):
    try:
        assert len(argv) > 2
    except:
        print_usage()
        sys.exit()

    if argv[1] == "--separate":
        try:
            assert len(argv) == 3
            assert argv[2].endswith(".fastq")
        except:
            print_usage()
            sys.exit()

    elif argv[1] == "--combine":
        try:
            assert len(argv) == 5
            assert argv[2].endswith(".fastq")
            assert argv[3].endswith(".fastq")
            assert argv[4].endswith(".fastq")
            assert argv[4] != argv[3] != argv[2]
        except:
            print_usage()
            sys.exit()

    elif argv[1] == "--devide":
        try:
            assert len(argv) == 4
            assert argv[2].endswith(".fastq")
            int(sys.argv[3])
        except:
            print_usage()
            sys.exit()

    elif argv[1] == "--fromlist":
        try:
            assert argv[2].endswith(".fastq")
        except:
            print_usage()
            sys.exit()

    else:
        print_usage()
        sys.exit()

def separate_combined_fastq(fastq_file):
    out_put_1 = fastq_file.replace(".fastq","_R1.fastq")
    out_put_2 = fastq_file.replace(".fastq","_R2.fastq")

    print "Start processing"
    count = -1
    for count,line in enumerate(open(fastq_file,"rU")):
        pass
    count += 1

    try:
        assert count%8==0
    except:
        print "this file contains %d lines,which isn't divisible by 8"%(count)
        assert count%8==0

    handle_fastq = open(fastq_file)
    handle_1 = open(out_put_1,"w")
    handle_2 = open(out_put_2,"w")

    j = 0
    percent = 0
    print "Start writing"
    while 1:
        for i in range(4):
            line = handle_fastq.readline()
            if line:
                handle_1.write(line)
        for i in range(4):
            line = handle_fastq.readline()
            if line:
                handle_2.write(line)
        if not line:
            break
        j += 1 
        if j * 8.0 / count > percent:
            print "%.2f%% finished"%(j*800.0/count)
            percent += 0.1
    handle_1.close()
    handle_2.close()

def combine_two_separate_reads_file(reads_1,reads_2,combined_reads):
    print "Start processing"
    #check Reads 1 has same length with Reads 2
    count_1 = -1
    for count_1,line in enumerate(open(reads_1,"rU")):
        pass
    count_1 += 1
    count_2 = -1
    for count_2,line in enumerate(open(reads_2,"rU")):
        pass
    count_2 += 1
    try:
        assert count_1 == count_2
    except:
        print "file 1 contains %d lines while file 2 contains % lines."\
                %(count_1,count_2)
        assert count_1 == count_2

    handle_1 = open(reads_1)
    handle_2 = open(reads_2)
    handle_w = open(combined_reads,"w")

    j = 0
    percent = 0
    print "Start writing"
    while 1:
        for i in range(4):
            line = handle_1.readline()
            if line:
                handle_w.write(line)
        for i in range(4):
            line = handle_2.readline()
            if line:
                handle_w.write(line)
        if not line:
            break
        j += 1 
        if j * 4.0 / count_1 > percent:
            print "%.2f%% finished"%(j*400.0/count_1)
            percent += 0.1
    handle_w.close()

def devide_fastq_to_n_parts(fastq,n):
    print "Start processing"
    count = -1
    for count,line in enumerate(open(fastq,"rU")):
        pass
    count += 1
    assert count%8 == 0

    part_len = math.ceil((count/8)*1.0/n)

    write_handles = []
    for i in range(n):
        write_file = fastq.replace(".fastq","_part%d.fastq"%(i+1))
        write_handles.append(open(write_file,"w"))

    read_handle = open(fastq)
    line = read_handle.readline()
    k = 0
    j = 0
    print "writing part %d"%(k+1)
    while line:
        if j == part_len:
            k += 1
            j = 0
            print "writing part %d"%(k+1)
        for i in range(8):
            write_handles[k].write(line)
            line = read_handle.readline()
        j += 1

def get_subset_from_list(fastq_file,sub_list_file):
    sub_dict = {}
    for line in open(sub_list_file):
        sub_dict[line.strip()] = 1

    cmd = "wc -l %s"%(fastq_file)
    count_line = os.popen(cmd).readline()
    count = int(count_line.strip().split(" ")[0])
    assert count%4 == 0
    os.system("purge")

    handle=open(fastq_file)
    j = 0
    percent = 0
    while 1:
        block = []
        for i in range(4):
            line = handle.readline()
            block.append(line.strip())
        if not line:
            break
        if block[0].split(" ")[0][1:] in sub_dict:
            print "\n".join(block)
        j += 1
        if j * 4.0 / count > percent:
            sys.stderr.write("%.2f%% finished\n"%(j*400.0/count))
            percent += 0.01
    os.system("purge")

def main():
    veriry_arguments(sys.argv)
    
    if sys.argv[1] == "--separate":
        fastq_file = sys.argv[2]
        separate_combined_fastq(fastq_file)
    elif sys.argv[1] == "--combine":
        reads_1 = sys.argv[2]
        reads_2 = sys.argv[3]
        out_put = sys.argv[4]
        combine_two_separate_reads_file(reads_1,reads_2,out_put)
    elif sys.argv[1] == "--devide":
        fastq = sys.argv[2]
        n = int(sys.argv[3])
        devide_fastq_to_n_parts(fastq,n)
    elif sys.argv[1] == "--fromlist":
        fastq_file = sys.argv[2]
        fastq_list = sys.argv[3]
        get_subset_from_list(fastq_file,fastq_list)
    else:
        print "This message should not appear"
        sys.exit()

if __name__ == "__main__":
    main()
