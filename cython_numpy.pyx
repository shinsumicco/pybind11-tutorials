import numpy as np

cimport cython
cimport numpy as np

def summation(np.ndarray[np.float64_t, ndim=1] X, np.ndarray[np.float64_t, ndim=1] Y):
    cdef double s = 0
    cdef double x, y
    for x in X:
        for y in Y:
            s += np.log10((x + y) ** 2) + np.sqrt(x * y)
    return s
