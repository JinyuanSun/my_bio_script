#!/usr/bin/env


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
            outfile.write(key+"\n"+fasta_dict[key])
            outfile.close()
    return filename
