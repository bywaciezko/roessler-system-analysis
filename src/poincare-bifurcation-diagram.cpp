#include "../headers/utils.hpp"
#include <fstream>
#include <iostream>
#include <vector>

using namespace capd;

void bf_diagram_data(std::vector<double> a_range, DVector x, int N) {
    std::ofstream a_out("output/tpw-bif-a.csv"), x_out("output/tpw-bif-x.csv");
    for (double a : a_range) {
        PoincareMap poincare(a);
        for (int t = 0; t < N; t++) {
            x = poincare.map(x);
            if (t > 250) {
                a_out << a << ",";
                x_out << x[1] << ",";
            }
        }
    }
    a_out.close();
    x_out.close();
}

int main() {
    int N = 1000;
    double return_time = 0;
    double initial_cond[] = {0, -5, 0.03};
    DVector x(3, initial_cond);

    // whole
    // std::vector<double> a_range = linspace<double>(2.5, 5.7, 2000);
    // first
    // std::vector<double> a_range = linspace<double>(4.379, 4.4, 350);
    // second
    // std::vector<double> a_range = linspace<double>(4.693, 4.725, 1000);
    // third
    std::vector<double> a_range = linspace<double>(5.17, 5.55, 1000);

    bf_diagram_data(a_range, x, N);
    return 0;
}
