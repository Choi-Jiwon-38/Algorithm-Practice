#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, m;
int count = 0;

void dfs(int x, int y, vector<vector<char> >& map, vector<vector<int> >& visit) {
    if (x < 0 || x >= n || y < 0 || y >= m || map[x][y] == 'X')
        return;
    
    if (visit[x][y] == 0) {
        // 방문 처리
        visit[x][y] = 1;

        if (map[x][y] == 'P') count++;

        dfs(x - 1, y, map, visit);
        dfs(x + 1, y, map, visit);
        dfs(x, y + 1, map, visit);
        dfs(x, y - 1, map, visit);


    }

}

int main() {
    cin >> n >> m;

    vector<vector<char> > map(n, vector<char>(m));
    vector<vector<int> > visit(n, vector<int>(m, 0));

    int x, y;

    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < m; j++) {
            map[i][j] = row[j];
            
            // 도연이의 시작 위치 저장
            if (row[j] == 'I') {
                x = i;
                y = j;
            }
        }
    }

    dfs(x, y, map, visit);

    cout << (count == 0 ? "TT" : to_string(count)) << '\n';

}