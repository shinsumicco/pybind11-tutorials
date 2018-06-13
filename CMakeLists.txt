cmake_minimum_required(VERSION 2.8)
project(test C CXX)

set(CMAKE_MACOSX_RPATH ON)
set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)
set(CMAKE_DISABLE_SOURCE_CHANGES  ON)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=c++11")

# Find dependencies
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIRS})

find_package(OpenMP)
if(OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

set(PYBIND11_CPP_STANDARD -std=c++11)
add_subdirectory("${test_SOURCE_DIR}/pybind11" "${test_SOURCE_DIR}/pybind11/build")

pybind11_add_module(cpp cpp.cc)
set_target_properties(cpp PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${test_SOURCE_DIR}/.")
pybind11_add_module(openmp_cpp openmp_cpp.cc)
set_target_properties(openmp_cpp PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${test_SOURCE_DIR}/.")