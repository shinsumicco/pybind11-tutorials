#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>

#include <Eigen/Core>

double summation(const Eigen::MatrixXd& X, const Eigen::MatrixXd& Y) {
    double s = 0;
    for (size_t i = 0; i < X.rows(); ++i) {
        for (size_t j = 0; j < Y.rows(); ++j) {
            if (0 < X(i) * Y(j)) {
                s += std::log10((X(i) + Y(j)) * (X(i) + Y(j))) + std::sqrt(X(i) * Y(j));
            }
        }
    }
    return s;
}

PYBIND11_MODULE(cpp, m) {
    m.def("summation", &summation);
}
