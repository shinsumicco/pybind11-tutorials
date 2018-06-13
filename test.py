import pure_numpy
import cython_numpy
import cpp
import openmp_cpp

import time

# ここは共通
import numpy as np
X = np.random.rand(1000)
Y = np.random.rand(5000)

print("pure numpy:")
start = time.time()
print("- sum: {}".format(pure_numpy.summation(X, Y)))
print("- elapsed: {}[s]".format(time.time() - start))
print("")

print("cython numpy:")
start = time.time()
print("- sum: {}".format(cython_numpy.summation(X, Y)))
print("- elapsed: {}[s]".format(time.time() - start))
print("")

print("cpp:")
start = time.time()
print("- sum: {}".format(cpp.summation(X, Y)))
print("- elapsed: {}[s]".format(time.time() - start))
print("")

print("openmp cpp:")
start = time.time()
print("- sum: {}".format(openmp_cpp.summation(X, Y)))
print("- elapsed: {}[s]".format(time.time() - start))
print("")
