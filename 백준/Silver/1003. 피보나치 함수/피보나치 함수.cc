#include <iostream>
#include <utility>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    pair<int, int> fibo[41];

    fibo[0] = make_pair(1, 0);
    fibo[1] = make_pair(0, 1);

    for (int i = 2; i <= 40; i++)
        fibo[i] = make_pair(fibo[i-1].first + fibo[i-2].first, fibo[i-1].second + fibo[i-2].second);

    int n, num;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> num;
        cout << fibo[num].first << " " << fibo[num].second  << '\n';
    }
}