#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    for(int k = 1; static_cast<float>(1 + pow(2, -k)) > 1; k++) {
        cout << pow(2, -k) << ", k = " << k << endl;
    }
    
    for(int k = 1; 1 + pow(2, -k) > 1; k++) {
        cout << pow(2, -k) << ", k = " << k << endl;
    }

    return 0;
}