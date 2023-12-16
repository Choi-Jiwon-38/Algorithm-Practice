#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int main()
{
    int N, K, W, V;
    cin >> N >> K;
    vector<pair<int, int>> items(N + 1);
    vector<vector<int>> P(N + 1, vector<int>(K + 1, 0));

    for (int i = 1; i <= N; i++)
    {
        cin >> W >> V;
        items[i] = {W, V};
    }

    for (int i = 1; i <= N; i++)     // i는 현재 선택한 물품
        for (int j = 1; j <= K; j++) // j는 현재 상태의 배낭 공간
        {
            if (items[i].first <= j) // i번째 물품이 선택될 수 있는 경우
            {
                P[i][j] = max(P[i - 1][j], P[i - 1][j - items[i].first] + items[i].second);
            }
            else // i번째 물품이 선택할 수 없는 경우
            {
                P[i][j] = P[i - 1][j];
            }
        }
    cout << P[N][K];
}