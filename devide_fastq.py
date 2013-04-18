#! /usr/bin/env python 
import os,sys
import math

#usage
#./separete_fastq.py XXXX.fastq n
#separete XXXX.fastq to n parts

fastq = sys.argv[1]
n = int(sys.argv[2])
path = "/".join((fastq.split("/")[:-1]))
assert os.path.exists(path)
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
    assert write_file not in os.listdir(path)
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
    
