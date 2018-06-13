import numpy as np

def summation(X, Y):
    s = 0
    for x in X:
        for y in Y:
            s += np.log10((x + y) ** 2) + np.sqrt(x * y)
    return s
