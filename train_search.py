__author__ = 'Tomasz'
import cPickle as pickle
import numpy as np

# Open both data (X) and output (Y)
with open('frames.txt', 'r') as f_x, open('frames_training.txt', 'r') as f_y:
    X = pickle.load(f_x)
    X = (X/255.0).astype(np.float32)
    Y_str = ', '.join([line.strip() for line in f_y.readlines()])
    Y = map(int, Y_str.split(', '))
    #print X[0, :].reshape(14, 10)
