import numpy as np

def summation(X, Y):
    s = 0
    for x in X:
        Y_matched = Y[0 < x * Y]
        l = np.log10((x + Y_matched) * (x + Y_matched)) + np.sqrt(x * Y_matched)
        s += np.sum(l)
    return s
