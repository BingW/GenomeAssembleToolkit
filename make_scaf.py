#! /usr/bin/env python
# coding:utf-8

#This Program aim at automatically order nodes, and generate ultra scaffold
#usage:
#./make_scaf.py ref_nt.fasta contigs.fasta

import sys
import os

ref_nt_fsa = sys.argv[1]
contig_fsa = sys.argv[2]
final_out = ref_nt_fsa+".final"

class Record():
    pass

#first run blast 
e_val = 0.00001

cmd = "makeblastdb -in %s -dbtype nucl -out %s"%(contig_fsa, contig_fsa+".db")
os.system(cmd)
cmd = "blastn -evalue %f -max_target_seqs 1 "%(e_val)+\
            "-db %s -query %s -out %s "%(contig_fsa+".db",ref_nt_fsa,ref_nt_fsa+".out") +\
            "-outfmt \"6 qseqid sseqid pident length mismatch gapopen qstart " +\
            "qend sstart send \""
os.system(cmd)
cmd = "rm %s"%contig_fsa+".db*"
os.system(cmd)
'''

#make gene decision(choose 1 best target)

handle = open(ref_nt_fsa+".out")
line = handle.readline()
r = Record()
qseqid,r.sseqid,r.pident,r.length,r.mismatch,r.gapopen,r.qstart,r.qend,r.sstart,r.send = line.split("\t")
gene_order = [qseqid]
gene2record = {qseqid:[r]}

for line in handle:
    r = Record()
    qseqid,r.sseqid,r.pident,r.length,r.mismatch,r.gapopen,r.qstart,r.qend,r.sstart,r.send = line.split("\t")
    if qseqid != gene_order[-1]:
        gene_order.append(qseqid)
        gene2record[qseqid] = [r]
    else:
        gene2record[qseqid].append(r)

for i,gene in enumerate(gene_order):
    if len(gene2record[gene]) > 1:
        up = gene_order[i-1]
        down = gene_order[i+1]
        if len(gene2record[up]) == 1 and len(gene2record[down]) == 1:
            if len([r for r in gene2record[gene] if r.sseqid == ])
        else:
            print "1:",gene


'''
