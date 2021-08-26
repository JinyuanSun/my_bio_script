
#!/usr/bin/env python
# -*- coding: UTF8 -*-

# By Jinyuan Sun
import structure


def read_msascanout(msa_out_file,cutoff=0.75):
    mut_list = []
    with open(msa_out_file) as scorefile:
        for line in scorefile:
            if line[0] == 'm':
                continue
            else:
                lst = line.split("\t")
                print(lst)
                score = float(lst[1])
                if score >= cutoff:
                    mutation = lst[0].split("_")
                    mut_list.append(mutation)
        scorefile.close()
    return mut_list

def read_cadesign_out(depect_out_file):
    mut_list = []
    with open(depect_out_file) as cafile:
        for line in cafile:
            if line[0] == "#":
                continue
            else:
                mut_list.append(line.split()[:-1])
        cafile.close()
    return mut_list


def output_modeller_resfile(mut_list,chain="A"):
    with open("modeller_resfile.txt","w+") as resfile:
        for mut in mut_list:
            resfile.write(str(mut[1]) + " " + structure._1_2_3(mut[2]) + " " + chain + "\n")
        resfile.close()

if __name__ == '__main__':
    import sys
    file = sys.argv[1]
    if file.endswith(".ca"):
        depect_out_file = file
        mut_list = read_cadesign_out(depect_out_file)
        output_modeller_resfile(mut_list,chain="A")
    else:
        msa_out_file = file
        try:
            cutoff = float(sys.argv[2])
            chain = sys.argv[3]
        except IndexError:
            print("msa_out_file is: "+msa_out_file+"\ncutoff = 0.75\nmaker mutation on A chain!")
        mut_list = read_msascanout(msa_out_file,cutoff=0.75)
        output_modeller_resfile(mut_list,chain="A")

