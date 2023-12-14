#include <vector>
#include <iostream>

using namespace std;

int main()
{
    int n, d, p;
    cin >> n;
    vector<int> dist;
    vector<int> price;
    int answer = 0;
    int subdist = 0;
    int subidx = 0;

    for (auto i = 0; i < n - 1; i++)
    {
        cin >> d;
        dist.push_back(d);
    }

    for (auto i = 0; i < n; i++)
    {
        cin >> p;
        price.push_back(p);
    }

    int cheap = price[0];
    for (int i = 0; i < n - 1; i++)
    {
        if (price[i] > price[i + 1] && cheap > price[i + 1])
        {
            for (int j = subidx; j <= i; j++)
            {
                subdist += dist[j];
            }
            answer += cheap * subdist;
            subdist = 0;
            subidx = i + 1;
            cheap = price[i + 1];
        }
        else
        {
            if (i == n - 2)
            {
                for (int j = subidx; j <= n - 1; j++)
                {
                    subdist += dist[j];
                }
                answer += cheap * subdist;
            }
        }
    }
    cout << answer;
}