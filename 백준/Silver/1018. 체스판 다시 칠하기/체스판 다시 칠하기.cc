#include <iostream>
using namespace std;

int calculate_board(char board[8][8]) {
    int count1 = 0;
    int count2 = 0;

    char curr;

    for (int i = 0; i < 8; i++) {
        curr = (i % 2 == 0) ? 'B' : 'W';

        for (int j = 0; j < 8; j++) {
            if (board[i][j] != curr) count1++;
            if (board[i][j] == curr) count2++;
            curr = (curr == 'W') ? 'B' : 'W';
        }
    }

    return (count1 < count2) ? count1 : count2;
}

int main() {
    int n, m;

    cin >> n >> m;

    char board[n][m];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> board[i][j];

    int min_count = __INT_MAX__;

    for (int i = 0; i < n - 7; i++)
        for (int j = 0; j < m - 7; j++) {
            char slice_board[8][8];

            for (int x = 0; x < 8; x++)
                for (int y = 0; y < 8; y++)
                    slice_board[x][y] = board[i + x][j + y]; 
            
            int result = calculate_board(slice_board);

            if (result < min_count)
                min_count = result;
        }

    cout << min_count;
}