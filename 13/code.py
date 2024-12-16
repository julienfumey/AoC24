import numpy as np
from scipy import linalg
import re

infile = "example.txt"

tokens_sum = 0
with open(infile, "r") as f:
    line = f.readline()
    while line:
        buttonA = line.strip()
        buttonB = f.readline().strip()
        results = f.readline().strip()
        line = f.readline()
        line = f.readline()

        valA = re.findall(r'X\+([0-9]+), Y\+([0-9]+)', buttonA)[0]
        valB = re.findall(r'X\+([0-9]+), Y\+([0-9]+)', buttonB)[0]
        val = np.array([[valA[0], valB[0]], [valA[1],valB[1]]], dtype=int)
        

        res =  re.findall(r'X\=([0-9]+), Y\=([0-9]+)', results)[0]
        prize = np.array([[int(res[0])], [int(res[1])]], dtype=int)

        #print(val, prize)
        X = linalg.solve(val, prize)
        print(X)

        xval = X[0][0]
        yval = X[1][0]
        print(xval, yval)
        if 0 <= xval < 100 and 0 <= yval < 100:
            tokens_sum += xval * 3 + yval
print(tokens_sum)