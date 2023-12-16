#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, k, p;
    cin >> n >> k;
    vector<int> coins;
    vector<int> answer(k + 1, 0);

    for (int i = 0; i < n; i++)
    {
        cin >> p;
        coins.push_back(p);
    }

    answer[0] = 1;

    for (int i = 0; i < n; i++)
        for (int j = 1; j <= k; j++)
            if (j - coins[i] >= 0)
                answer[j] += answer[j - coins[i]];

    cout << answer[k];
}