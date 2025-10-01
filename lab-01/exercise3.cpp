#include <iostream>
#include <cmath>
#include <limits>
#include <iomanip>

using namespace std;

double stable_procedure(double x) {
    if (fabs(x) < 1e-3) {
        return pow(x, 3) / 6.0 - pow(x, 5) / 120.0 + pow(x, 7) / 5040.0;
    }
	else {
        return x - sin(x);
    }
}

int main() {
    cout << setprecision(20);

    double test_vals[] = {1e-1, 1e-5, 1e-8, 1.0};
    for (double x : test_vals) {
        double naive = x - sin(x);
        double stable = stable_procedure(x);

        cout << "x = " << x << "\n";
        cout << "  naive      = " << naive << "\n";
        cout << "  stable     = " << stable << "\n";
        cout << "  difference = " << fabs(naive - stable) << "\n\n";
    }

    return 0;
}
