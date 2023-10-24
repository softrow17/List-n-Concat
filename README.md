# List-n-Concat
A python executable script to speed up some of my bioinformatic processing.

This python executable can be used to search a directory containing fasta files, find partial matches to the contents of a .CSV list document, and then concatenate those matching fasta files into a single file for further processing. 

The current format of my values in the input list is NAME.NUM, with the name of the fasta files being NAME.NUM.EXTRA_INFO_NOT_NEEDED.fasta. Based on this formatting, the script looks for a partial match by splitting the fasta file names after the second '.' character. This gives a match with input=file (NAME.NUM == NAME.NUM). This matching criteria can be changed based on formatting requirements.

The executable takes two input options:
1. "bin_list" - the CSV file containg a list of input values, the current use case for me is a list of genomic bin names
2. "input_directory" - this is the path to the directory cintaing the fasta files of interest

To run simply use:

    list_n_concat.py /PATH/TO/INPUT.CSV /PATH/TO/FASTAS/

Output: the output will be a directory (currently called /drep_bin_pacbio_16s/ - this can be changed in the script) conating a concatenated single fasta file of all the matching fasta input files.




