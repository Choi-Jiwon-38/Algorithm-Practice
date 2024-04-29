#include <iostream>

using namespace std;

int Max(int a, int b)
{
    return a > b ? a : b;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;

    cin >> n;

    int stair[n];
    int dp[n];

    fill_n(dp, n, 0);

    for (int i = 0; i < n; i++)
        cin >> stair[i];

    dp[0] = stair[0];
    dp[1] = stair[0] + stair[1];
    dp[2] = Max(stair[0] + stair[2], stair[1] + stair[2]);

    for (int i = 3; i < n; i++)
    {
        dp[i] = Max(stair[i] + dp[i - 2], stair[i] + stair[i - 1] + dp[i - 3]);
    }

    cout << dp[n - 1] << '\n';
}