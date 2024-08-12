'''
Filters the blast results to select those fulfilling user-specified conditions
(see 'config.yaml') and then calls multiple sequence alignment (MSA) on them. At the 
moment this uses MUSCLE to perform the MSA, but could be easily changed to use e.g., ClustalW.

Planned developments include integration of Python plugins which can be supplied by the user for
more advanced functionality

A. Vargas Richards, 09.08.2024
'''

import pandas as pd
import os


def tabulate(summary_file): # first convert the summary file to a pandas dataframe
    fwf = pd.read_fwf(summary_file)
    print(fwf)
    return

def make_filter(config_file, plugin): # construct filter rules to apply to the dataframe
    # read in configuration file 


    return filtered_data

def apply_filter(dataframe, filter_rules): # apply the specified filter rules to the dataframe

    return new_df # return the filtered results




def test():
    # initial_modifier = os.path.join('..')
    
    os.chdir('..')
    input_path = os.path.join('..','archive','testdata', 'summary')

    with open(input_path, 'r') as inp:
        line_array = []
        for line in inp:
            #print(line)
            for part in line:
                first = line.split(' ')[0]
                identity = first.split('_')[0]                
                print(part,'\n')
                print(f'Identity is {identity}')
    # print(os.listdir())
    # tabulate('')
    return df # returns a pandas dataframe with the data
test()

'''
What will the fields in the dataframe be ....

'''