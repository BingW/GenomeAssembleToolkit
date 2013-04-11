#! /usr/bin/env python
# coding utf-8
import os
import sys

'''
Useage:
Put all reads file in to your work_dir
By now only two seperate fastq file could be recognized, otherwise will report error
to use, simply type ./run_velvet.py work_dir
'''

work_dir = sys.argv[1]
work_dir = work_dir + "/" if not work_dir.endswith("/") else work_dir
assert os.path.exists(work_dir)
fastqs = [work_dir+f for f in os.listdir(work_dir) if f.endswith(".fastq")]
if len(fastqs) == 2:
    sepORnot = "-separate"
elif len(fastqs) == 1:
    sepORnot = "-interleaved"
else:
    sepORnot = "-interleaved"
k = 63
cmd = "velveth %s %d -fastq -shortPaired %s %s "%(work_dir,k,sepORnot," ".join(fastqs))
os.system(cmd)
cmd = "velvetg %s -exp_cov auto -shortMatePaired yes"%(work_dir)
os.system(cmd)


