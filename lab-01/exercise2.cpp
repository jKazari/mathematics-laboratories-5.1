#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    for (int k = 0; k < 20; k++) {
        double x = pow(8, -k);
        cout << sqrt(x*x + 1) - 1 << endl;
        cout << (x*x)/(sqrt(x*x + 1) + 1) << endl << endl;
    }

    return 0;
    
    // Wiarygodne są wyniki z funkcji g, ponieważ unikamy odejmowania bliskich sobie liczb
}