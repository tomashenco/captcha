__author__ = 'Tomasz'
import os
import numpy as np
from matplotlib import pyplot as plt

# Get input file paths
input_path = os.getcwd() + '\input'
input_files = [f for f in os.listdir(input_path) if 'txt' in f]
# Get output file paths
output_path = os.getcwd() + '\output'
output_files = [f for f in os.listdir(output_path) if 'txt' in f]

# Read all files and combine them in pairs - input, output
for in_file, out_file in zip(input_files, output_files):
    with open(os.path.join(input_path, in_file), 'r') as in_f, open(os.path.join(output_path, out_file), 'r') as out_f:
        # Get size of image
        rows, cols = map(int, in_f.readline().strip().split())
        # Read the rest of lines to get list
        mat = [line.split(',') for x in in_f.readlines() for line in x.strip().split()]
        # Convert to Numpy mat
        np_mat = np.array(mat, np.uint8).reshape((rows, cols, 3))
        # # Optional to show image
        # plt.imshow(np_mat)
        # plt.show()

        # Read output
        output = out_f.readline()
