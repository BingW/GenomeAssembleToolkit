#! /usr/bin/env python 
#coding:utf-8
#this program can do combine,separate,devide fastq file(s)

import os,sys

def print_usage():
    print "\nUsage:\n"
    print "To separate an intergrated paired fastq file into Reads1.fastq and Reads2.fastq."
    print "$./bing_paired_fastq --separate fastq_to_be_separate\n"
    print "To combine separated Reads_1 and Reads_2 into one intergrated fastq file"
    print "$./bing_paired_fastq --combine Reads_1 Reads_2 out_put_combined_fastq\n"
    print "To devide an intergrated paired fastq file into n parts"
    print "$./bing_paired_fastq --devide fastq_to_be_devide n\n"
try:
    assert len(sys.argv) > 2
except:
    print_usage()
    sys.exit()

if sys.argv[1] == "--separate":
    try:
        assert len(sys.argv) == 3
        fastq_file = sys.argv[2]
        assert fastq_file.endswith(".fastq")
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

    except:
        print_usage()

elif sys.argv[1] == "--combine":
    try:
        assert len(sys.argv) == 5
        fastqs = sys.argv[2:4]
        out_put = sys.argv[4]
        assert out_put not in fastqs

        print "Start processing"
        count_1 = -1
        for count_1,line in enumerate(open(fastqs[0],"rU")):
            pass
        count_1 += 1
        count_2 = -1
        for count_2,line in enumerate(open(fastqs[0],"rU")):
            pass
        count_2 += 1
        try:
            assert count_1 == count_2
        except:
            print "file 1 contains %d lines while file 2 contains % lines."\
                    %(count_1,count_2)
            assert count_1 == count_2

        handle_1 = open(fastqs[0])
        handle_2 = open(fastqs[1])
        handle_w = open(out_put,"w")

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

    except:
        print_usage()

elif sys.argv[1] == "--devide":
    import math
    try:
        assert len(sys.argv) == 4
        fastq = sys.argv[2]
        n = int(sys.argv[3])

        assert fastq.endswith(".fastq")

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
    except:
        print_usage()

else:
    print_usage()
