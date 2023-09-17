import numpy as np
import scipy.io
from Bio import SeqIO
from itertools import product

from scipy.io import savemat, loadmat


def generate_n_mers(n):
    nucleotides = ["A", "T", "C", "G"]
    n_mers = [''.join(mer) for mer in product(nucleotides, repeat=n)]
    return n_mers

def read_mat_file(file_path):
    try:
        data = scipy.io.loadmat(file_path)
        return data
    except FileNotFoundError:
        print(f"The MAT file '{file_path}' does not exist.")
        return None

fasta_file = r"C:\Users\acer\Desktop\New folder (3)\B.1.429.fasta"
sequences = list(SeqIO.parse(fasta_file, "fasta"))

n = int(input("Enter the sequence length to be displayed: "))

headers = [sequence.description for sequence in sequences]

n_mers = generate_n_mers(n)


data_dict = {}

for row_index, header in enumerate(headers, start=2):
    sequence = next(seq for seq in sequences if seq.description == header)
    sequence_text = str(sequence.seq)
    for col_index, n_mer in enumerate(n_mers, start=2):
        n_mer_count = 0
        for i in range(len(sequence_text) - n + 1):
            if sequence_text[i:i+n] == n_mer:
                n_mer_count += 1
        data_dict[f"{header}_{n_mer}"] = n_mer_count


savemat('data.mat', data_dict)

print(f"MAT file 'data.mat' has been created.")

def load_and_display_mat(file_path):

    loaded_data = loadmat(file_path)


    for key, value in loaded_data.items():
        print(f"{key}: {value}")

print(f"File 'data.mat' has been updated .")
load_and_display_mat('data.mat')