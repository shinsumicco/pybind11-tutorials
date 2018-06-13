from distutils.core import setup
from Cython.Build import cythonize
import numpy
 
setup(
     ext_modules = cythonize("cython_numpy.pyx"),
     include_dirs = [numpy.get_include()]
)

import os
import errno
import subprocess

def mkdir_p(path):
    try:
        os.makedirs(path)
    except os.error as exc:
        if exc.errno != errno.EEXIST or not os.path.isdir(path):
            raise

print("Configuring...")
mkdir_p("build")
subprocess.Popen(["cmake", ".."], cwd="build").wait()

print("Compiling extension...")
subprocess.Popen(["make", "-j4"], cwd="build").wait()