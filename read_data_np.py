import numpy as np

f = open("data/data.npy", "r")

lines = f.readlines()

for line in lines:
    print(line)
