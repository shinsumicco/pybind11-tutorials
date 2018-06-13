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
elapsed_times = []
for i in range(iteration):
    start = time.time()
    pure_numpy.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    elapsed_times.append(elapsed)
print("- average: {0:.8f} [s]".format(np.average(elapsed_times)))
print("- median:  {0:.8f} [s]".format(np.median(elapsed_times)))
print("- maximum: {0:.8f} [s]".format(np.max(elapsed_times)))
print("- minimum: {0:.8f} [s]".format(np.min(elapsed_times)))
print("")

print("cython numpy:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    cython_numpy.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    elapsed_times.append(elapsed)
print("- average: {0:.8f} [s]".format(np.average(elapsed_times)))
print("- median:  {0:.8f} [s]".format(np.median(elapsed_times)))
print("- maximum: {0:.8f} [s]".format(np.max(elapsed_times)))
print("- minimum: {0:.8f} [s]".format(np.min(elapsed_times)))
print("")

print("cpp:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    cpp.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    elapsed_times.append(elapsed)
print("- average: {0:.8f} [s]".format(np.average(elapsed_times)))
print("- median:  {0:.8f} [s]".format(np.median(elapsed_times)))
print("- maximum: {0:.8f} [s]".format(np.max(elapsed_times)))
print("- minimum: {0:.8f} [s]".format(np.min(elapsed_times)))
print("")

print("openmp cpp:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    openmp_cpp.summation(X, Y)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.8f} [s]".format(i + 1, elapsed))
    elapsed_times.append(elapsed)
print("- average: {0:.8f} [s]".format(np.average(elapsed_times)))
print("- median:  {0:.8f} [s]".format(np.median(elapsed_times)))
print("- maximum: {0:.8f} [s]".format(np.max(elapsed_times)))
print("- minimum: {0:.8f} [s]".format(np.min(elapsed_times)))
