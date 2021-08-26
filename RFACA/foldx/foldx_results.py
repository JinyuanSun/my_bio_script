#!/usr/bin/python

#By Sun Jinyuan and Cui Yinglu, 2021

import pandas as pd
import argparse

parser = argparse.ArgumentParser(description=
                                 'Process files from previous foldx scan')
parser.add_argument("-sn", '--subdirnum', help="Total number of subdirectories")
parser.add_argument("-fn", '--fxoutname', help="Average_BuildModel_<pdbfilename>.fxout")
parser.add_argument("-c", '--cutoff',help="Cutoff of ddg")

args = parser.parse_args()

fxoutname = args.fxoutname
subnum = int(args.subdirnum)
cutoff = int(args.cutoff)

df_average_lst = []
for num in range(subnum):
    num += 1
    fxout_name = "Subdirectory"+str(num)+"/"+fxoutname
    df_average = pd.read_table(fxout_name, sep='\t',skiprows=8)
    df_average_lst.append(df_average)
    
    
df_list_lst = []
for num in range(subnum):
    num += 1
    list_name = "test/Subdirectory"+str(num)+"/List_Mutations_readable.txt"
    df_list = pd.read_table(list_name, sep=" ",header=None)
    df_list_lst.append(df_list)

    
df_average_all = pd.concat(df_average_lst, axis=0, ignore_index=True)
#df_average.head()
df_list_all = pd.concat(df_list_lst, axis=0, ignore_index=True)
df_o = df_average_all.iloc[:, 0:3].join(df_list_all)
odict = {'mutation':[],'energy':[],'SD':[],'position':[]}
for i in range(df_o.shape[0]):
    odict['mutation'].append(str(df_o[1][i])+str(df_o[2][i])+str(df_o[3][i]))
    odict['position'].append(str(df_o[2][i]))
    odict['energy'].append(df_o['total energy'][i])
    odict['SD'].append(df_o['SD'][i])
    
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

BelowCutOff_df = BelowCutOff(CompleteList_df,-1)

BelowCutOff_SortedByEnergy_df = BelowCutOff(CompleteList_SortedByEnergy_df,-1)

BestPerPositionBelowCutOff_SortedByEnergy_df = BelowCutOff(BestPerPosition_SortedByEnergy_df,-1)

BestPerPositionBelowCutOff_df = BelowCutOff(BestPerPosition_df,-1)

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


