__author__ = 'Tomasz'
import os
import numpy as np
from sklearn import svm

from matplotlib import pyplot as plt
from matplotlib import cm

# Get input file paths
input_path = os.getcwd() + '\input'
input_files = [f for f in os.listdir(input_path) if 'txt' in f]
# Get output file paths
output_path = os.getcwd() + '\output'
output_files = [f for f in os.listdir(output_path) if 'txt' in f]

X = []
Y = []
# Read all files and combine them in pairs - input, output
for in_file, out_file in zip(input_files, output_files):
    with open(os.path.join(input_path, in_file), 'r') as in_f:
        rows, cols = map(int, in_f.readline().strip().split())
        # Read the rest of lines to get list
        mat = [line.split(',') for x in in_f.readlines() for line in x.strip().split()]
        # Convert to Numpy array
        np_mat = np.array(mat, np.float32).reshape((rows, cols, 3))
        # Convert to greyscale
        np_mat = (np_mat[:, :, 0]*0.299 + np_mat[:, :, 1]*0.587 + np_mat[:, :, 2]*0.114).astype(np.uint8)
        # Threshold at 50
        np_mat[np_mat > 50] = 255

        # Step in pixels for sliding window
        step = 1
        width = 10
        for i in range(0, cols-width, step):
            frame = np_mat[9:-7, i:i+width]
            # Optional to show image
            plt.imshow(frame, cmap=cm.Greys_r)
            plt.show()

    with open(os.path.join(output_path, out_file), 'r') as out_f:
        # Read output
        output = out_f.readline()
        Y.append(output)
