#include <iostream>

using namespace std;

int main()
{
    int n, m, x, y, z;

    cin >> n >> m;

    int ball[n];

    fill_n(ball, n, 0);

    for (int i = 0; i < m; i++)
    {
        cin >> x >> y >> z;

        for (int j = x - 1; j < y; j++)
            ball[j] = z;
    }

    for (int i = 0; i < n; i++)
        cout << ball[i] << " ";
    cout << '\n';
}