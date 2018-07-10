# pybind11-tutorials

Comparion of calculation speeds of pure numpy, cython and C++ wrapper

## Dependencies

- Required
    - Compiler
        - Required: C++11 support
    - Eigen
        - Recommended: version 3.3 or later
    - Python
        - Required: 3.5 or later
        - Required: Cython
- Recommended
    - OpenMP

 ## Preparation

 ```bash
$ python --version
Python 3.6.4
$ git clone https://github.com/shinsumicco/pybind11-tutorials --recursive
$ cd pybind11-tutorials/class_wrapping/
$ python setup.py build
$ cd ../multiple_loop/
$ python setup.py build
 ```

## Run

```bash
$ pwd
/path/to/pybind11-tutorials/class_wrapping
$ python test.py 
size: 0
[]

size: 1
[1]

size: 3
[1, 5, 24]

size: 13
[1, 5, 24, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

$
```

```bash
$ pwd
/path/to/pybind11-tutorials/multiple_loop
$ python test.py 
pure numpy 1:
- iteration   1: 7892.45796 [ms]
- average: 7892.45796 [ms]
- median:  7892.45796 [ms]
- maximum: 7892.45796 [ms]
- minimum: 7892.45796 [ms]

pure numpy 2:
- iteration   1: 82.02696 [ms]
- average: 82.02696 [ms]
- median:  82.02696 [ms]
- maximum: 82.02696 [ms]
- minimum: 82.02696 [ms]

cython numpy:
- iteration   1: 85.24299 [ms]
- average: 85.24299 [ms]
- median:  85.24299 [ms]
- maximum: 85.24299 [ms]
- minimum: 85.24299 [ms]

cython libmath:
- iteration   1: 44.65175 [ms]
- average: 44.65175 [ms]
- median:  44.65175 [ms]
- maximum: 44.65175 [ms]
- minimum: 44.65175 [ms]

cpp:
- iteration   1: 57.65295 [ms]
- average: 57.65295 [ms]
- median:  57.65295 [ms]
- maximum: 57.65295 [ms]
- minimum: 57.65295 [ms]

openmp cpp:
- iteration   1: 21.88301 [ms]
- average: 21.88301 [ms]
- median:  21.88301 [ms]
- maximum: 21.88301 [ms]
- minimum: 21.88301 [ms]
$
```
