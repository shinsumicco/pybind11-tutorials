import pure_numpy
import cython_numpy
import cpp
import openmp_cpp

import sys
import time

# ここは共通
import numpy as np
X = np.random.rand(1000)
Y = np.random.rand(5000)

if 2 <= len(sys.argv):
    iteration = int(sys.argv[1])
else:
    iteration = 1

print("pure numpy:")
sum = 0
for i in range(iteration):
    start = time.time()
    pure_numpy.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    sum += elapsed
print("- average: {0:.8f} [s]".format(sum / iteration))
print("")

print("cython numpy:")
sum = 0
for i in range(iteration):
    start = time.time()
    cython_numpy.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    sum += elapsed
print("- average: {0:.8f} [s]".format(sum / iteration))
print("")

print("cpp:")
sum = 0
for i in range(iteration):
    start = time.time()
    cpp.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    sum += elapsed
print("- average: {0:.8f} [s]".format(sum / iteration))
print("")

print("openmp cpp:")
sum = 0
for i in range(iteration):
    start = time.time()
    openmp_cpp.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    sum += elapsed
print("- average: {0:.8f} [s]".format(sum / iteration))
