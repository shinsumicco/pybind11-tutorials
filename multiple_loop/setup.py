import os
import sys
import errno
import numpy
import subprocess
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


def mkdir_p(path):
    try:
        os.makedirs(path)
    except os.error as exc:
        if exc.errno != errno.EEXIST or not os.path.isdir(path):
            raise

build = False
clean = False

if 2 <= len(sys.argv):
    if sys.argv[1] == "build" or sys.argv[1] == "build_ext":
        build = True
    elif sys.argv[1] == "clean":
        clean = True
    else:
        print("Undefined command: {}".format(sys.argv[1]))
        exit(1)
else:
    print("Prease specify a command: build, clean")
    exit(1)

if build:
    sys.argv[1] = "build_ext"

setup(
    ext_modules = [Extension("cython_numpy", ["cython_numpy.pyx"])],
    cmdclass = {"build_ext": build_ext},
    include_dirs = [numpy.get_include()]
)

if build:
    print("Configuring...")
    mkdir_p("build")
    subprocess.Popen(["cmake", "..",
                      "-DCMAKE_BUILD_TYPE=Release",
                      "-DCMAKE_C_FLAGS=-fopenmp -L/usr/local/opt/llvm/lib/",
                      "-DCMAKE_CXX_FLAGS=-fopenmp -L/usr/local/opt/llvm/lib/"],
                     cwd="build").wait()
    print("Compiling extension...")
    subprocess.Popen(["make", "-j4"], cwd="build").wait()

if clean:
    print("Removing...")
    subprocess.Popen(["rm", "-r", "build"], cwd=os.path.join("./", os.path.dirname(sys.argv[0]))).wait()
