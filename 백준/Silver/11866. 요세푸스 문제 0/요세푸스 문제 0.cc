#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, k;

    cin >> n >> k;

    queue<int> q;
    vector<int> v;

    for (int i = 1; i <= n; i++)
        q.push(i);

    while (!q.empty()) {
        for (int i = 0; i < k -1; i++) {
            int front_num = q.front();
            q.pop();
            q.push(front_num);
        }

        int front_num = q.front();
        q.pop();
        v.push_back(front_num);
    }

    cout << "<";
    for (int i = 0; i < n; i++) {
        cout << v[i];
        if (i != n-1) cout << ", ";
    }
    cout << ">";
}