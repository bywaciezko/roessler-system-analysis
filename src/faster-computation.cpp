#include "../headers/utils.hpp"

bool pw_bound_parallel(const std::vector<interval> &a_range, IVector x,
                       interval &bound, int N, int period, bool find_lower) {
    bool found = false;
    std::mutex mtx;

    auto worker = [&](const std::vector<interval> &chunk) {
        for (const auto &a : chunk) {
            RosslerSystem rossler(a);
            if (rossler.is_periodic_and_stable(x, N, period)) {
                std::lock_guard<std::mutex> lock(mtx);
                if (!found || (find_lower && a < bound) ||
                    (!find_lower && a > bound)) {
                    bound = a;
                    found = true;
                }
                break;
            }
        }
    };

    int num_threads = 10;
    std::vector<std::thread> threads;
    std::vector<std::vector<interval>> chunks(num_threads);

    for (int i = 0; i < a_range.size(); ++i) {
        chunks[i % num_threads].push_back(a_range[i]);
    }

    for (int i = 0; i < num_threads; ++i) {
        if (!chunks[i].empty()) {
            threads.emplace_back(worker, std::cref(chunks[i]));
        }
    }

    for (auto &t : threads)
        t.join();

    return found;
}
void pw_lower_bound(std::vector<interval> a_range, IVector x,
                    interval &lower_bound, int N, int period) {
    bool found = pw_bound_parallel(a_range, x, lower_bound, N, period, true);
}
