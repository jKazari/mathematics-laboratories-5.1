#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    cout << setprecision(20);

    for (int k = 0; k < 16; k++) {
        double x = pow(8.0, -k);
        double f = sqrt(x*x + 1.0) - 1.0;
        double g = (x*x) / (sqrt(x*x + 1.0) + 1.0);

        cout << "x = 8^(-" << k << ")" << "\n";
        cout << "  f(x) = " << f << "\n";
        cout << "  g(x) = " << g << "\n\n";
    }

    return 0;
}

// Wiarygodne są wyniki z g(x), ponieważ wyniki z f(x) psują się dla małych x, 
// bo pojawia się utrata cyfr znaczących przy odejmowaniu bliskich sobie liczb.
