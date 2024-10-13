#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n, m;

    cin >> n >> m;

    map<string, string> p;

    string site, password;

    for (int i = 0; i < n; i++) {
        cin >> site >> password;
        p[site] = password;
    }

    for (int i = 0; i < m; i++) {
        cin >> site;
        auto it = p.find(site);
        if (it != p.end()) {
            cout << it->second << '\n';
        }
    }
}
