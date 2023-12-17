#include <iostream>
#include <cstring>

using namespace std;
int LCS[1001][1001];
int SAVE[1001][1001];

void printLCS(int m, int n, char S[])
{
    if (m == 0 || n == 0)
        return;

    int path = SAVE[m][n];

    if (path == 1)
    {
        printLCS(m - 1, n - 1, S);
        cout << S[m - 1];
    }
    else if (path == 2)
        printLCS(m - 1, n, S);
    else
        printLCS(m, n - 1, S);
}

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
            {
                SAVE[i][j] = 1;
                LCS[i][j] = LCS[i - 1][j - 1] + 1;
            }
            else
            {
                int l, r;
                l = LCS[i - 1][j];
                r = LCS[i][j - 1];

                if (l > r)
                {
                    SAVE[i][j] = 2;
                    LCS[i][j] = l;
                }
                else
                {
                    SAVE[i][j] = 3;
                    LCS[i][j] = r;
                };
            }

    cout << LCS[lenS][lenT] << '\n';
    printLCS(lenS, lenT, S);
}