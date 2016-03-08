__author__ = 'Tomasz'
import os
import numpy as np
import cPickle as pickle

# Get input file paths
input_path = os.getcwd() + '\input'
input_files = [f for f in os.listdir(input_path) if 'txt' in f]

X = []
# Read all files and combine them in pairs - input, output
for in_file in input_files:
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
            frame = np_mat[9:-7, i:i+width].flatten()
            X.append(frame)

X = np.array(X)
with open('frames.txt', 'w') as f:
    pickle.dump(X, f)