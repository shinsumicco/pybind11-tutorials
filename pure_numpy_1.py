import numpy as np

def summation(X, Y):
    s = 0
    for x in X:
        for y in Y:
            if 0 < x * y:
                s += np.log10((x + y) * (x + y)) + np.sqrt(x * y)
    return s
