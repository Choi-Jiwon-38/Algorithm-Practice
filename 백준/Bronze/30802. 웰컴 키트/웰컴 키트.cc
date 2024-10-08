#include <iostream>

using namespace std;

int main() {
    int sizes[6];

    int n, t, p;

    cin >> n;

    for (int i = 0; i < 6; i++) {
        cin >> sizes[i];
    }

    cin >> t >> p;

    int count = 0;

    for (int i = 0; i < 6; i++) {
        count += sizes[i] / t;

        if (sizes[i] % t != 0)
            count++;
    }

    cout << count << '\n';
    cout << n / p << " " << n % p;
}   
