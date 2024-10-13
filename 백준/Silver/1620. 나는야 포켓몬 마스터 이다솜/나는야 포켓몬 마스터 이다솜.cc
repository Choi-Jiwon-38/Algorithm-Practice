#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios_base::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;

    map<string, string> poketmon;

    string name;

    for (int i = 1; i <= n; i++) {
        cin >> name;
        string no = to_string(i);
        poketmon[no] = name;
        poketmon[name] = no;
    }

    string target;

    for (int i = 0; i < m; i++) {
        cin >> target;
        auto it = poketmon.find(target);
        if (it != poketmon.end()) {
            cout << it->second << '\n';
        }
    }
}