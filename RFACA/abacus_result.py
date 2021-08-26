#!/usr/bin/python

# By Jinyuan Sun, 2021

#A   43 VAL->LYS SAI: 0.666 S1: -0.035 S2:  0.000 PACK:   1.180 TOTAL:   1.145
#A   43 VAL->LEU SAI: 0.666 S1:  0.288 S2:  0.000 PACK:   1.612 TOTAL:   1.900

from mbs.basic import structure

CUTOFF = 3

def read_abacus_file(abacus_file):
    abacus_score_dict = {}
    with open(abacus_file) as abacus_file:
        for line in abacus_file:
            lst = line.strip().split()
            res_num = lst[1]
            mutation = lst[2]
            score = float(lst[-1])
            wild = structure._3_2_1(mutation[0:3])
            mut = structure._3_2_1(mutation[-3:])
            key = wild + "_" + res_num + "_" + mut
            abacus_score_dict[key] = score
            #print(key, score)
        abacus_file.close()
    return abacus_score_dict

def dump_tabfile(abacus_score_dict,cutoff):
    for key in abacus_score_dict:
        if abacus_score_dict[key] < cutoff:
            

read_abacus_file("6JTT.pdb1.abacus2.out")
