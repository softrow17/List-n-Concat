import csv
import os
import argparse
from Bio import SeqIO


# Script to take list of bin names, search directory for fasta's containg bin name, concatenate fasta files into one file

parser = argparse.ArgumentParser(description="Find FASTA files for concatenation.")
parser.add_argument("bin_list", help="CSV file with list of bin names")
parser.add_argument("input_directory", help="Directory containing the FASTA files of interest")

# Parse the command-line arguments
args = parser.parse_args()

# Create an output directory to store 16S rRNA FASTQ files
output_directory = os.path.join(args.input_directory, "drep_bin_pacbio_16s")
os.makedirs(output_directory, exist_ok=True)

# Function to find fasta files that match the bin names
def find_matching_fasta_files(bin_names, directory):
    matching_fasta_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".fasta"):
                # Extract the bin name up to the second dot
                bin_name_in_file = file.split(".")[0] + "." + file.split(".")[1]

                for bin_name in bin_names:
                    # Check if the extracted bin name matches any bin name from the list
                    if bin_name == bin_name_in_file:
                        matching_fasta_files.append(os.path.join(root, file))
    return matching_fasta_files

# Function to concatenate fasta files into a single file
def concatenate_fasta_files(input_files, output_file):
    with open(output_file, 'w') as output_handle:
        for input_file in input_files:
            for record in SeqIO.parse(input_file, 'fasta'):
                SeqIO.write(record, output_handle, 'fasta')

bin_names = []
with open (args.bin_list, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        bin_names.extend(row)

# Find matching FASTA files to the bin names
bin_match_fasta = find_matching_fasta_files(bin_names, args.input_directory)

if bin_match_fasta:
    # Output file to save the concatenated sequences
    output_file = "all_drep_16s.fasta"
    output_path = os.path.join(output_directory, output_file)

    # Concatenate the matching fasta files into a single file
    concatenate_fasta_files(bin_match_fasta, output_path)

    print(f"Concatenated {len(bin_match_fasta)} fasta files into {output_path}")
else:
    print("No matching fasta files found.")