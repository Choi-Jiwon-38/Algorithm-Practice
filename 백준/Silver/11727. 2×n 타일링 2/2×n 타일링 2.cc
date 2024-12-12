#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<int> v(n + 1);

    // base case
    v[1] = 1;
    v[2] = 3;

    // recursive case
    for (int i = 3; i <= n; i++)
        v[i] = (2 * v[i - 2] + v[i - 1]) % 10007;
    
    cout << v[n];
}
