#! /usr/bin/env python
#coding: utf-8
import os ,sys
#combine two seperated paired fastq file into one file
assert len(sys.argv) == 4
fastqs = sys.argv[1:3]
out_put = sys.argv[3]
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

