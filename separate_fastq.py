#! /usr/bin/env python
#coding: utf-8
import os ,sys
#seperated combined paired fastq file into two files
assert len(sys.argv) == 2
fastq_file = sys.argv[1]
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

