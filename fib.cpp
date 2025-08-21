#include <bits/stdc++.h>
using namespace std;

uint64_t fib_iter(int n) {
    if (n <= 1) return n;
    uint64_t a = 0, b = 1;
    for (int i = 2; i <= n; ++i) {
        uint64_t c = a + b;
        a = b;
        b = c;
    }
    return b;
}

uint64_t fib_rec(int n) {
    if (n <= 1) return n;
    return fib_rec(n-1) + fib_rec(n-2);
}

int main(int argc, char** argv) {
    if (argc < 5) {
        cerr << "Usage: ./fib <iter|rec> <n> <repeats> <csv_out>\n";
        return 1;
    }
    string mode = argv[1];
    int n = stoi(argv[2]);
    int repeats = stoi(argv[3]);
    string csv_out = argv[4];

    vector<double> times_ms;
    times_ms.reserve(repeats);

    for (int r = 0; r < repeats; ++r) {
        auto start = chrono::high_resolution_clock::now();
        volatile uint64_t res = 0;
        if (mode == "iter") {
            res = fib_iter(n);
        } else if (mode == "rec") {
            res = fib_rec(n);
        } else {
            cerr << "mode must be iter|rec\n";
            return 2;
        }
        auto end = chrono::high_resolution_clock::now();
        double ms = chrono::duration<double, std::milli>(end - start).count();
        times_ms.push_back(ms);
    }

    double avg = accumulate(times_ms.begin(), times_ms.end(), 0.0) / times_ms.size();

    // append CSV line
    ofstream f(csv_out, ios::app);
    f << "compiled_cpp," << (mode == "iter" ? "iterative" : "recursive")
      << "," << n << "," << repeats << "," << fixed << setprecision(6) << avg << "\n";

    return 0;
}
