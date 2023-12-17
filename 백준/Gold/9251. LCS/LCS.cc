#include <iostream>
#include <cstring>

using namespace std;
int LCS[1001][1001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    char S[1001];
    char T[1001];

    cin >> S >> T;

    int lenS = strlen(S);
    int lenT = strlen(T);

    for (int i = 1; i <= lenS; i++)
        for (int j = 1; j <= lenT; j++)
            if (S[i - 1] == T[j - 1])
                LCS[i][j] = LCS[i - 1][j - 1] + 1;
            else
            {
                int l, r;
                l = LCS[i - 1][j];
                r = LCS[i][j - 1];

                LCS[i][j] = (l > r) ? l : r;
            }

    cout << LCS[lenS][lenT];
}