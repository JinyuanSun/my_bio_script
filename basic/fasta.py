#!/usr/bin/env python
# By Jinyuan Sun


def fasta2dic(fastafilename): #read a fasta file into a dict
    fasta_dict = {}
    with open(fastafilename) as fastafile:
        for line in fastafile:
            if line[0] == ">":
                head = line.strip()
                fasta_dict[head] = ''
            else:
                fasta_dict[head] += line.strip()
        fastafile.close()
    return fasta_dict

def output_single_fa(fasta_dict): #split a fastadict into fasta file of single seq
    for key in fasta_dict:
        filename = key[1:]+".fa"
        with open(filename, "w+") as outfile:
            outfile.write(key+"\n"+fasta_dict[key]+"\n")
            outfile.close()
    return filename

def split_fasta(fastafilename):
    output_single_fa(fasta2dic(fastafilename))

def read_a3m():

    return []

def align_2_seq(raw_seq1,raw_seq2):

    from Bio import pairwise2
    import pickle
    with open("BLOSUM62.pkl", "rb") as tf:
        matrix = pickle.load(tf)
        tf.close()

    seq1 = raw_seq1
    seq2 = raw_seq2

    alignments = pairwise2.align.globalds(seq1, seq2, matrix, -10, -0.5)
    seq1 = alignments[0][0]
    seq2 = alignments[0][1]
    resnum = 0
    #index = 0
    aligned_seq2 = ''
    for index in range(len(seq1)):
        if seq1[index] == "-":
            continue
        else:
            aligned_seq2 += seq2[index]
            resnum += 1
            if seq1[index] == seq2[index]:
                continue
            #else:
                #print(seq1[index],resnum,seq2[index])
        index += 1
    #print(raw_seq1+"\n"+aligned_seq2)
    return aligned_seq2

