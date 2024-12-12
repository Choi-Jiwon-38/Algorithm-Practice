#include <iostream>
#include <vector>
using namespace std;

int countW = 0;
int countB = 0;
vector<vector<int> > v(129, vector<int>(129));

void fc(int x, int y, int k) {
    bool cut = false;
    int color = v[x][y];

    for (int i = x; i < x + k; i++)
        for (int j = y; j < y + k; j++) {
            if (v[i][j] != color) {
                cut = true;
                break;
            }
        }
    
    if (cut) {
        int nextK = k / 2;
        fc(x, y, nextK);
        fc(x, y + nextK, nextK);
        fc(x + nextK, y, nextK);
        fc(x + nextK, y + nextK, nextK);
    } else {
        if (color == 1) {
            countB++;
        } else {
            countW++;
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> v[i][j];

    fc(0, 0, n);

    cout << countW << '\n';
    cout << countB << '\n';
}