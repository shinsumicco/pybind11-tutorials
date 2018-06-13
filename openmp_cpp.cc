#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>

#include <Eigen/Core>

#include <iostream>

double summation(const Eigen::MatrixXd& X, const Eigen::MatrixXd& Y) {
#ifndef _OPENMP
    std::cerr << "Warning: OpenMP is disabled." << std::endl;
#endif
    double s = 0;
    size_t i, j;
#ifdef _OPENMP
#pragma omp parallel for private(j) reduction(+:s)
#endif
    for (i = 0; i < X.rows(); ++i) {
        for (j = 0; j < Y.rows(); ++j) {
            s += std::log10((X(i) + Y(j)) * (X(i) + Y(j))) + std::sqrt(X(i) * Y(j));
        }
    }
    return s;
}

PYBIND11_MODULE(openmp_cpp, m) {
    m.def("summation", &summation);
}
