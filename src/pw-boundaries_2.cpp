#include "../headers/utils.hpp"

static const char *menu =
    "======================================================"
    "====\n"
    "|| Ktore okno mierzymy?\n"
    "|| 1. pierwsze \n"
    "|| 2. drugie \n"
    "|| 3. trzecie \n"
    "======================================================"
    "====\n";

static const char *prompt = "wybor: ";
static const char *interlude =
    "======================================================"
    "====\n";
void pw_lower_bound(interval &lower_bound, interval &left, interval &right,
                    IVector &x, int N, interval eps, int period) {
    interval mid;
    while ((right - left) >= eps) {
        mid = (left + right) / interval(2.0);
        RosslerSystem rossler(mid);
        if (rossler.is_periodic_and_stable(x, N, period, false)) {
            lower_bound = mid;
            right = mid;
        } else
            left = mid;
    }
}

int main() {
    cout.precision(16);

    int N = 300;
    interval eps = 1e-9;
    std::string s_time = "Time";

    try {
        cout << boolalpha;

        int input;
        do {
            cout << menu;
            cout << prompt;
            cin >> input;
            cout << '\n';

            switch (input) {
            case 1: {
                IVector p_close_to_6_periodic(
                    {-7.459016042357787, 0.03638246580414306});
                double period = 6;

                // ======== lower bound ========
                interval lower_bound;
                interval left = interval(4.38);
                interval right = interval(4.381);

                measure_time(s_time, [&]() {
                    pw_lower_bound(lower_bound, left, right,
                                   p_close_to_6_periodic, N, eps, period);
                });

                RosslerSystem rossler(lower_bound);

                if (rossler.is_periodic_and_stable(p_close_to_6_periodic, N,
                                                   period, true)) {
                    std::cout << "Lower bound: " << lower_bound << '\n';
                } else {
                    std::cout << "Lower bound couldn't be established\n";
                }

                // Czas wykonania: 101.885464817 sekund
                // ograniczenie dolne: 4.380026185035703
                break;
            };
            case 2: {
                IVector p_close_to_5_periodic(
                    {-8.723283653276134, 0.03382484879611583});

                double period = 5;

                // ======== lower bound ========
                interval lower_bound;
                interval left = interval(4.694);
                interval right = interval(4.695);

                measure_time(s_time, [&]() {
                    pw_lower_bound(lower_bound, left, right,
                                   p_close_to_5_periodic, N, eps, period);
                });

                RosslerSystem rossler(lower_bound);
                if (rossler.is_periodic_and_stable(p_close_to_5_periodic, N,
                                                   period, true)) {
                    std::cout << "Lower bound: " << lower_bound << '\n';
                } else {
                    std::cout << "Lower bound couldn't be established\n";
                }

                // Czas wykonania: 85.526941522 sekund
                // ograniczenie dolne: [4.694104184150694, 4.694104184150699]

                break;
            }
            case 3: {
                IVector p_close_to_3_periodic(
                    {-3.562081704612412, 0.03491621098889878});

                double period = 3;

                // ======== lower bound ========
                interval lower_bound;
                interval left = interval(5.185);
                interval right = interval(5.186);

                pw_lower_bound(lower_bound, left, right, p_close_to_3_periodic,
                               N, eps, period);

                RosslerSystem rossler(lower_bound);
                if (rossler.is_periodic_and_stable(p_close_to_3_periodic, N,
                                                   period, true)) {
                    std::cout << "Lower bound: " << lower_bound << '\n';
                } else {
                    std::cout << "Lower bound couldn't be established\n";
                }

                // Czas wykonania: 55.289916007 sekund
                // ograniczenie dolne: [5.185404746055601, 5.185404746055606]
                break;
            }
            default:
                break;
            }
        } while (input == 1 || input == 2 || input == 3);

    } catch (exception &e) {
        cout << "\n\nException: " << e.what() << endl;
    }
    return 0;
}
