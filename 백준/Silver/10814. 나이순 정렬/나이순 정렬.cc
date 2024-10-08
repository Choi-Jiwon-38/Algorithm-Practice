#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool compare(pair<int, string> a, pair<int, string> b) {
    return a.first < b.first;
}

int main() {
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios_base::sync_with_stdio(false);

    int n, age;
    string name;
    cin >> n;

    vector<pair<int, string> > users;

    for (int i = 0; i < n; i++) {
        cin >> age >> name;
        users.push_back(make_pair(age, name));
    }

    stable_sort(users.begin(), users.end(), compare);

    for (int i = 0; i < n; i++) {
        cout << users[i].first << " " << users[i].second << '\n';
    }

}