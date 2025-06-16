#include "../headers/utils.hpp"
#include <fstream>
#include <iostream>
#include <vector>

using namespace capd;
void plot_data(double a, DVector x, int N) {
    std::ofstream y_out("output/y_output.csv"), py_out("output/py_output.csv");

    PoincareMap poincare(a);
    for (int i = 0; i < N; i++) {
        y_out << x[1] << ",";
        x = poincare.map(x);
        py_out << x[1] << ",";
    }

    y_out.close();
    py_out.close();
}

int main() {
    int N = 1000;
    double return_time = 0, a = 5.25;
    double initial_cond[] = {0, -5, 0.03};
    DVector x(3, initial_cond);

    plot_data(a, x, N);
    return 0;
}
