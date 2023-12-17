#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, K, A;
    int answer = 0;
    cin >> N >> K;
    vector<int> coins;

    while (N--)
    {
        cin >> A;
        coins.push_back(A);
    }

    for (int i = coins.size() - 1; i >= 0; i--)
    {
        while (K >= coins[i])
        {
            K -= coins[i];
            answer++;
        }

        if (K == 0)
            break;
    }

    cout << answer;
}