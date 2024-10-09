#include <iostream>
#include <string>
using namespace std;

int main() {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios_base::sync_with_stdio(false);
    int v[21];
    fill_n(v, 21, 0);

    int n, m;
    string cmd;
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> cmd;
        if (cmd != "all" && cmd != "empty") cin >> n;

        if (cmd == "add") {
            v[n] = 1;
        } else if (cmd == "remove") {
            v[n] = 0;
        } else if (cmd == "toggle") {
            v[n] = v[n] ? 0 : 1;
        } else if (cmd == "all") {
            fill_n(v, 21, 1);
        } else if (cmd == "empty") {
            fill_n(v, 21, 0);
        } else if (cmd == "check") {
            cout << v[n] << '\n';
        }
    }
}
