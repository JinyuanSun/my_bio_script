#!/usr/bin/env python



def _3_2_1(x):
    d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
         'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
         'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
         'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    y = d[x]
    return y

def _1_2_3(oneletteraa):
    aadict = {
        'C': "CYS",
        'D': "ASP",
        'S': "SER",
        'N': "ASN",
        'K': "LYS",
        'I': "ILE",
        'P': "PRO",
        'T': "THR",
        'F': "PHE",
        'Q': "GLN",
        'G': "GLY",
        'H': "HIS",
        'L': "LEU",
        'R': "ARG",
        'W': "TRP",
        'A': "ALA",
        'V': "VAL",
        'E': "GLU",
        'Y': "TYR",
        'M': "MET"
    }
    return aadict[oneletteraa]


