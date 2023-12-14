#include <stdio.h>
#include <utility>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    return (a.second == b.second) ? a.first < b.first : a.second < b.second;
}

int main()
{
    int n, s, e;
    int last = 0; // 마지막으로 회의가 끝난 시간
    int answer = 0;
    vector<pair<int, int>> room;

    scanf("%d", &n);
    while (n--)
    {
        scanf("%d %d", &s, &e);
        room.push_back({s, e});
    }

    sort(room.begin(), room.end(), compare);

    for (pair<int, int> r : room)
    {
        if (r.first >= last)
        {
            last = r.second;
            answer++;
        }
    }
    printf("%d", answer);
}