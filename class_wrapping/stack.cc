#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

class stack {
public:
    stack() = default;
    virtual ~stack() = default;
    void push(const int n) { v_.push_back(n); }
    unsigned int get_size() { return v_.size(); }
    std::vector<int> get_stacked() { return v_; }
private:
    std::vector<int> v_;
};

PYBIND11_MODULE(stack, m) {
    pybind11::class_<stack> st(m, "stack");
    st.def(pybind11::init<>());
    st.def("push", &stack::push);
    st.def("get_size", &stack::get_size);
    st.def("get_stacked", &stack::get_stacked);
}
