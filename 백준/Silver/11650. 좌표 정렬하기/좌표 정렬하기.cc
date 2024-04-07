#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.first == b.first)
    {
        return a.second < b.second;
    }
    return a.first < b.first;
}

int main()
{
    int n, x, y;
    vector<pair<int, int> > dots;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        dots.push_back(make_pair(x, y));
    }

    sort(dots.begin(), dots.end(), compare);

    for (int i = 0; i < n; i++)
    {
        cout << dots[i].first << " " << dots[i].second << '\n';
    }
}