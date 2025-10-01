#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    cout << setprecision(20);

    // Dla float
    float eps_f = 1.0f;
    int kf = 0;
    while (1.0f + eps_f / 2.0f > 1.0f) {
        eps_f /= 2.0f;
        kf++;
    }
    cout << "Epsilon (float)  = " << eps_f << "   dla k = " << kf << "\n";

    // Dla double
    double eps_d = 1.0;
    int kd = 0;
    while (1.0 + eps_d / 2.0 > 1.0) {
        eps_d /= 2.0;
        kd++;
    }
    cout << "Epsilon (double) = " << eps_d << "   dla k = " << kd << "\n";

    return 0;
}
