#!/usr/bin/python

# By Jinyuan Sun, 2021


from mbs.basic import structure
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description=
                                 'Process files from previous ABACUS2 singleMutScan')
parser.add_argument("-ao", '--abacusoutfile', help="Output of ABACUS file")
parser.add_argument("-c", '--cutoff',help="Cutoff of ABACUS score")

args = parser.parse_args()

abacus_file = args.abacusoutfile
CUTOFF = int(args.cutoff)


def read_abacus_file(abacus_file):
    mutation_list = []
    position_list = []
    energy_list = []
    SD_list = []
    with open(abacus_file) as abacus_file:
        for line in abacus_file:
            lst = line.strip().split()
            res_num = lst[1]
            mutation = lst[2]
            score = float(lst[-1])
            wild = structure._3_2_1(mutation[0:3])
            mut = structure._3_2_1(mutation[-3:])
            key = wild + res_num + mut
            mutation_list.append(key)
            position_list.append(res_num)
            energy_list.append(score)
            SD_list.append(0)
            #abacus_score_dict[key] = score
            #print(key, score)
        abacus_file.close()
    return {'mutation':mutation_list,'energy':energy_list,'SD':SD_list,'position':position_list,}

odict = read_abacus_file(abacus_file)
CompleteList_df = pd.DataFrame(odict)

CompleteList_SortedByEnergy_df = CompleteList_df.sort_values('energy').reset_index(drop=True)

def BetsPerPosition(df):
    position_list = []
    length = df.shape[0]
    for i in range(length):
        if df['position'][i] in position_list:
            df = df.drop(index=i)
        else:
            position_list.append(df['position'][i])
    return df.reset_index(drop=True)

def BelowCutOff(df,cutoff):
    #position_list = []
    length = df.shape[0]
    for i in range(length):
        if float(df['energy'][i]) > float(cutoff):
            df = df.drop(index=i)
        else:
            continue
    return df.reset_index(drop=True)

BestPerPosition_SortedByEnergy_df = BetsPerPosition(CompleteList_SortedByEnergy_df)

BestPerPosition_df = BetsPerPosition(CompleteList_SortedByEnergy_df)

BelowCutOff_df = BelowCutOff(CompleteList_df,-CUTOFF)

BelowCutOff_SortedByEnergy_df = BelowCutOff(CompleteList_SortedByEnergy_df,-CUTOFF)

BestPerPositionBelowCutOff_SortedByEnergy_df = BelowCutOff(BestPerPosition_SortedByEnergy_df,-CUTOFF)

BestPerPositionBelowCutOff_df = BelowCutOff(BestPerPosition_df,-CUTOFF)

def variablename(var):
    import itertools
    return [tpl[0] for tpl in filter(lambda x: var is x[1], globals().items())]


def out_tab_file(df):
    df_name = variablename(df)[0]
    filename = "MutationsEnergies_"+df_name[:-3]+".tab"
    with open(filename,"w+") as of:
        of.write(BestPerPositionBelowCutOff_df.to_csv(columns=['mutation', 'energy', 'SD'], sep='\t', index=False))
        of.close()

out_tab_file(CompleteList_df)
out_tab_file(CompleteList_SortedByEnergy_df)
out_tab_file(BestPerPosition_SortedByEnergy_df)
out_tab_file(BestPerPosition_df)
out_tab_file(BelowCutOff_df)
out_tab_file(BelowCutOff_SortedByEnergy_df)
out_tab_file(BestPerPositionBelowCutOff_SortedByEnergy_df)
out_tab_file(BestPerPositionBelowCutOff_df)



