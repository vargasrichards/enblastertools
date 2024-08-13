# Calls MUSCLE on the results of the BLAST search.
# A. Vargas Richards, NIAB 29.07.2024

# easily customisable for more specialised forms of MSA.
# added modification to filter
# todo, parallelisation if desired. 13.08.2024

import subprocess, os
import multiprocessing

# Parallelism using process map .

def single_msa(file):
    outfile = "BLAST-results/MSA_results/" + str(file)
    infile = "BLAST-results/" + str(file)
    subprocess.Popen(["muscle", "-in", infile, "-out", outfile])
    return


def call_msa(results_folder): # calls muscle on all of the 
    os.mkdir(str(results_folder) + "/MSA_results")
    for root, dirs, files in os.walk(results_folder):
        for file in files:
            if ".fasta" in file:
                print(f"Attemnpting subprocess.Popen for {file}")
                single_msa(file)
    return


def parallel_msa(results_folder): # call parallised MSA using Pool
    valid_files = []
    aligners= multiprocessing.Pool() # first we initialise the Pool of worker processes
    for root, dirs, files in os.walk(results_folder):
        for file in files:
            if ".fasta" in file:
                valid_files.append(file)
        multiprocessing.map_async(single_msa, valid_files)
    return 

