import numpy as np

cimport cython
cimport numpy as cnp
from libc.math cimport log10, sqrt

cdef extern from "math.h" nogil:
    cnp.float64_t log10(cnp.float64_t)
cdef extern from "math.h" nogil:
    cnp.float64_t sqrt(cnp.float64_t)

@cython.wraparound(False)
@cython.boundscheck(False)
def summation(cnp.ndarray[cnp.float64_t, ndim=1] X, cnp.ndarray[cnp.float64_t, ndim=1] Y):
    cdef cnp.float64_t s = 0
    cdef cnp.int_t i, j
    with nogil:
        for i in range(X.shape[0]):
            for j in range(Y.shape[0]):
                if 0 < X[i] * Y[j]:
                    s += log10((X[i] + Y[j]) * (X[i] + Y[j])) + sqrt(X[i] * Y[j])
    return s
