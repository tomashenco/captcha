__author__ = 'Tomasz'
import os

input_path = os.getcwd() + '\input'
files = [f for f in os.listdir(input_path) if 'txt' in f]
print files
