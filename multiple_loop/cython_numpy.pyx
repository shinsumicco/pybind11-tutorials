import numpy as np

cimport cython
cimport numpy as cnp

@cython.wraparound(False)
@cython.boundscheck(False)
def summation(cnp.ndarray[cnp.float64_t, ndim=1] X, cnp.ndarray[cnp.float64_t, ndim=1] Y):
    cdef cnp.float64_t s = 0
    cdef cnp.float64_t x, y
    cdef cnp.ndarray[cnp.float64_t, ndim=1] Y_matched, l
    for x in X:
        Y_matched = Y[0 < x * Y]
        l = np.log10((x + Y_matched) * (x + Y_matched)) + np.sqrt(x * Y_matched)
        s += np.sum(l)
    return s
