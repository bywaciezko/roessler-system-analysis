#include "../headers/utils.hpp"
PoincareMap::PoincareMap(double a)
    : rossler("par:a,b;var:x,y,z;fun:-(y+z),x+b*y,b+z*(x-a);"),
      solver(rossler, 20), section(3, 0),
      map(solver, section, poincare::MinusPlus) {
    rossler.setParameter("a", a);
    rossler.setParameter("b", 2. / 10.);
}

IVector SectionMap::image(IVector &x, IMatrix &DP, int period) {
    IVector X({0., 0., 0.});
    X[1] = x[0];
    X[2] = x[1];

    C1Rect2Set Q(X);
    IMatrix DP3(3, 3);

    IVector Y = (*P)(Q, DP3, period);
    DP3 = P->computeDP(Y, DP3, period);

    IVector y(2);
    y[0] = Y[1];
    y[1] = Y[2];
    return y;
}

IVector SectionMap::image(IVector &x, int period) {
    IVector X({0., 0., 0.});
    X[1] = x[0];
    X[2] = x[1];

    C0Rect2Set Q(X);

    IVector Y = (*P)(Q, period);

    IVector y(2);
    y[0] = Y[1];
    y[1] = Y[2];

    return y;
}

IMatrix SectionMap::derivative(IVector &x, int period) {
    IMatrix DP(2, 2);
    image(x, DP, period);
    return DP;
}

vector<interval> eigenvalues2x2(IMatrix &M) {
    interval a = M[0][0];
    interval b = M[0][1];
    interval c = M[1][0];
    interval d = M[1][1];

    interval trace = a + d;
    interval det = a * d - b * c;
    interval discriminant = sqrt(sqr(trace) - 4 * det);

    interval lambda1 = (trace + discriminant) / 2;
    interval lambda2 = (trace - discriminant) / 2;

    return {lambda1, lambda2};
}

bool RosslerSystem::has_smaller_period(IVector &point, int period) {
    for (int d = 1; d < period; ++d) {
        if (period % d == 0) {
            IVector image = poincare_2d(point, d);
            if (subset(image, point)) {
                cout << "The point has a smaller fundamental period: " << d
                     << '\n';
                return true;
            }
        }
    }

    cout << "Period " << period << " is the fundamental period of the point.\n";
    return false;
}
bool RosslerSystem::is_periodic_and_stable(IVector &initial_guess, int N,
                                           int period, bool is_final_check) {
    IVector current_guess = initial_guess;
    IVector poincare_image, prev_guess, verified_point(2);
    IMatrix Id = IMatrix({{1., 0.}, {0., 1.}});
    IMatrix dp(2, 2);

    int steps = 0;
    try {
        while (true) {
            current_guess = midVector(current_guess);
            prev_guess = current_guess;

            poincare_image = poincare_2d(current_guess, dp, period);
            current_guess =
                current_guess - gauss(dp - Id, poincare_image - current_guess);

            ++steps;
            if (subset(prev_guess, current_guess) || steps >= N)
                break;
        }

        if (steps < N) {
            double delta = 1e-9;
            IVector small_box(2);
            small_box[0] = current_guess[0] + delta * interval(-1.0, 1.0);
            small_box[1] = current_guess[1] + delta * interval(-1.0, 1.0);

            poincare_2d(small_box, dp, period);

            verified_point = current_guess -
                             gauss(dp - Id, poincare_2d(current_guess, period) -
                                                current_guess);

            if (subsetInterior(verified_point, small_box)) {

                // STABILITY CHECK
                poincare_2d(verified_point, dp, period);
                auto eigenvalues = eigenvalues2x2(dp);

                bool is_stable = true;
                for (const auto &eig : eigenvalues) {
                    if (abs(mid(eig)) >= 1.0) {
                        is_stable = false;
                        break;
                    }
                }

                // SPRAWDZENIE CZY NIE MA MNIEJSZEGO OKRESU
                if (is_final_check) {
                    std::cout << "A stationary point for P^" << period
                              << " is in " << verified_point << " proven. \n";

                    std::cout << "The periodic orbit is "
                              << (is_stable ? "stable." : "unstable.") << '\n';

                    return !has_smaller_period(verified_point, period);
                }

                return is_stable;
            }
        } else {
        }
    } catch (const exception &e) {
        cout << "Exception caught for initial guess " << initial_guess << ": "
             << e.what() << endl;
    }

    return false;
}
