import math
import pandas


def readFile(filename):
    f = open(filename, 'r')
    print(f.read())


def fillArray(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    return data


filename = "var4.txt"
#readFile(filename)
data = fillArray(filename)
print(data)
