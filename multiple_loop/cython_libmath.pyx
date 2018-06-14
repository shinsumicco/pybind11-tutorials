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
    cdef cnp.float64_t x
    cdef cnp.int_t j
    cdef cnp.ndarray[cnp.float64_t, ndim=1] Y_matched
    for x in X:
        Y_matched = Y[0 < x * Y]
        with nogil:
            for j in range(Y_matched.shape[0]):
                s += log10((x + Y_matched[j]) * (x + Y_matched[j])) + sqrt(x * Y_matched[j])
    return s
