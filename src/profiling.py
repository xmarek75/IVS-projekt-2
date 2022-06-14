from LibMath import *
import sys


def mean(data):
    return float(div(sum(data), len(data)))

def variance(data):
    mu = mean(data)
    return mean([power((sub(x, mu)), 2) for x in data])

def stddev(data):
    return root(variance(data), 2)

numbers = sys.stdin.read()

data = numbers.split()

for i in range(len(data)):
    data[i] = float(data[i])

x = stddev(data)

print(x)

