cmake_minimum_required(VERSION 2.8)
project(class_wrapping C CXX)

set(CMAKE_MACOSX_RPATH ON)
set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)
set(CMAKE_DISABLE_SOURCE_CHANGES  ON)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=c++11")

set(PYBIND11_CPP_STANDARD -std=c++11)
add_subdirectory("${class_wrapping_SOURCE_DIR}/../pybind11" "${class_wrapping_SOURCE_DIR}/../pybind11/build")

pybind11_add_module(stack stack.cc)
set_target_properties(stack PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${class_wrapping_SOURCE_DIR}/.")
