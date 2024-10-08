#include <iostream>
using namespace std;

int main() {
    int n, k; 
    cin >> n >> k;

    int num1 = 1;
    int num2 = 1;

    for (int i = 1; i <= k; i++) {
        num1 *= n;
        num2 *= i;
        n--;
    }

    cout << num1 / num2;
}