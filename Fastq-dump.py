'''
Script done by:
Bruno Lopes 202000210
Gonçalo Cachado 202000190
Ioana Chichirita 202000180
Rodrigo Silva 202000193
Samuel Correia 202000094
Turma: Binf21
'''
import sys
import subprocess

file_name = sys.argv[1]

def read_file(file_name):
    '''
    Opens the file with the name passed through the parameter file_name.
    Reads the file_name file and stores the lines in the list file_lines.
    The list file_lines is returned.
    '''
    with open(file_name) as user_file:
        file_lines = user_file.readlines()
    user_file.close()
    return(file_lines)

def number_normalizer(file_lines):
    '''
    Gets the file lines passed through the parameter file_lines.
    Eliminates the characters '\n' from all the sra numbers in the file lines 
    and stores them in the list sra_numbers.
    The list sra_numbers is returned.
    '''    
    sra_numbers = [x.replace('\n','') for x in file_lines]
    return(sra_numbers)

def prefetching(sra_numbers):
    '''
    **************************************************************************************************
    *Title: python-fastq-downloader
    *Author: Erick Lu
    *Date: March 17, 2022
    *Availability: Lu, E. (2022). GitHub - erilu/python-fastq-downloader: 
    *A guide on how to find and download raw RNA-seq data from GEO. 
    *Batch download FASTQ files using a Python script and the NCBI SRA tools prefetch and fastq-dump.. 
    *GitHub. Retrieved 28 June 2022, from https://github.com/erilu/python-fastq-downloader.
    **************************************************************************************************
    The list containing the sra numbers is passed through
    the parameter sra_numbers.
    The list sra_numbers is iterated, dowloading/prefetching each time a sra file from
    the variable sra_number using the prefetch command in the shell from SRA toolkit.
    '''
    for sra_number in sra_numbers:
        print ("Dowloading sra file: " + sra_number)
        prefetch = "prefetch " + sra_number
        print ("The command used: " + prefetch)
        subprocess.call(prefetch, shell=True)
    print('Prefetching complete.')

def fastq(sra_numbers):
    '''
    **************************************************************************************************
    *Title: python-fastq-downloader
    *Author: Erick Lu
    *Date: March 17, 2022
    *Availability: Lu, E. (2022). GitHub - erilu/python-fastq-downloader: 
    *A guide on how to find and download raw RNA-seq data from GEO. 
    *Batch download FASTQ files using a Python script and the NCBI SRA tools prefetch and fastq-dump.. 
    *GitHub. Retrieved 28 June 2022, from https://github.com/erilu/python-fastq-downloader.
    **************************************************************************************************
    The list containing the sra numbers is passed through
    the parameter sra_numbers.
    The list sra_numbers is iterated, generating each time a fastq file 
    from the prefetched sra file from the variable sra_number using the
    fastq_dump commeand in the shell from SRA toolkit.
    '''
    for sra_number in sra_numbers:
        print("Generating fastq for: " + sra_number)
        fastq_dump = "fastq-dump " + sra_number
        print ("The command used: " + fastq_dump)
        subprocess.call(fastq_dump, shell=True)
    print('Fastq generation complete.')

file_lines = read_file(file_name)
sra_numbers = number_normalizer(file_lines)

prefetching(sra_numbers)
fastq(sra_numbers)
