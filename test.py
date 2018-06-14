import pure_numpy_1
import pure_numpy_2
import cython_numpy
import cpp
import openmp_cpp

import sys
import time

# ここは共通
import numpy as np
X = np.random.rand(1000) * 2.0 - 1
Y = np.random.rand(5000) * 2.0 - 1

if 2 <= len(sys.argv):
    iteration = int(sys.argv[1])
else:
    iteration = 1

print("pure numpy 1:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    s = pure_numpy_1.summation(X, Y)
    print(s)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.5f} [ms]".format(i + 1, elapsed * 1000))
    elapsed_times.append(elapsed * 1000)
print("- average: {0:.5f} [ms]".format(np.average(elapsed_times)))
print("- median:  {0:.5f} [ms]".format(np.median(elapsed_times)))
print("- maximum: {0:.5f} [ms]".format(np.max(elapsed_times)))
print("- minimum: {0:.5f} [ms]".format(np.min(elapsed_times)))
print("")

print("pure numpy 2:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    s = pure_numpy_2.summation(X, Y)
    print(s)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.5f} [ms]".format(i + 1, elapsed * 1000))
    elapsed_times.append(elapsed * 1000)
print("- average: {0:.5f} [ms]".format(np.average(elapsed_times)))
print("- median:  {0:.5f} [ms]".format(np.median(elapsed_times)))
print("- maximum: {0:.5f} [ms]".format(np.max(elapsed_times)))
print("- minimum: {0:.5f} [ms]".format(np.min(elapsed_times)))
print("")

print("cython numpy:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    s = cython_numpy.summation(X, Y)
    print(s)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.5f} [ms]".format(i + 1, elapsed * 1000))
    elapsed_times.append(elapsed * 1000)
print("- average: {0:.5f} [ms]".format(np.average(elapsed_times)))
print("- median:  {0:.5f} [ms]".format(np.median(elapsed_times)))
print("- maximum: {0:.5f} [ms]".format(np.max(elapsed_times)))
print("- minimum: {0:.5f} [ms]".format(np.min(elapsed_times)))
print("")

print("cpp:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    s = cpp.summation(X, Y)
    print(s)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.5f} [ms]".format(i + 1, elapsed * 1000))
    elapsed_times.append(elapsed * 1000)
print("- average: {0:.5f} [ms]".format(np.average(elapsed_times)))
print("- median:  {0:.5f} [ms]".format(np.median(elapsed_times)))
print("- maximum: {0:.5f} [ms]".format(np.max(elapsed_times)))
print("- minimum: {0:.5f} [ms]".format(np.min(elapsed_times)))
print("")

print("openmp cpp:")
elapsed_times = []
for i in range(iteration):
    start = time.time()
    s = openmp_cpp.summation(X, Y)
    print(s)
    elapsed = time.time() - start
    print("- iteration {0:>3}: {1:.5f} [ms]".format(i + 1, elapsed * 1000))
    elapsed_times.append(elapsed * 1000)
print("- average: {0:.5f} [ms]".format(np.average(elapsed_times)))
print("- median:  {0:.5f} [ms]".format(np.median(elapsed_times)))
print("- maximum: {0:.5f} [ms]".format(np.max(elapsed_times)))
print("- minimum: {0:.5f} [ms]".format(np.min(elapsed_times)))
