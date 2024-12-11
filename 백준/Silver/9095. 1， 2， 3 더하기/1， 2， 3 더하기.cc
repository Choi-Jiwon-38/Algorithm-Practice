#include <iostream>
#include <vector>

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;

    cin >> t;

    while (t--) {
        cin >> n;
        vector<int> v(n + 1);

        // base case
        v[0] = 1;
        v[1] = 1;
        v[2] = 2;

        if (n <= 2) {
            cout << v[n] << '\n';
            continue;
        }

        // recursive case
        for (int i = 3; i <= n; i++)
            v[i] = v[i - 3] + v[i - 2] + v[i -1];

        cout << v[n] << '\n';
    }
}
