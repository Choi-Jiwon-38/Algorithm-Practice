#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> P;
    int N, p;
    int answer = 0;
    int wait = 0;
    scanf("%d", &N);

    while (N--)
    {
        scanf("%d", &p);
        P.push_back(p);
    }
    sort(P.begin(), P.end());

    for (int p : P)
    {

        answer += wait + p;
        wait += p;
    }
    printf("%d\n", answer);
}