#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    int n, len = 0;
    scanf("%d", &n);

    int A[n + 1], dp[n + 1];
    A[0] = 0;
    fill_n(dp, n + 1, 0);

    for (int i = 1; i <= n; i++)
        scanf("%d", &A[i]);

    for (int i = 1; i <= n; i++)
        for (int j = 0; j < i; j++)
            if (A[i] > A[j])
                dp[i] = max(dp[i], dp[j] + 1);

    for (int i = 1; i <= n; i++)
        len = max(len, dp[i]);

    printf("%d", len);
}