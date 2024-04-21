#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int X, N, a, b;
    int total = 0;

    cin >> X >> N;

    while (N--)
    {
        cin >> a >> b;
        total += a * b;
    }

    (total == X) ? cout << "Yes" : cout << "No";
}