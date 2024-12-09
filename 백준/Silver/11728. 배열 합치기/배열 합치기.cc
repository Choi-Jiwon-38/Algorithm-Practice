#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m;
    cin >> n >> m;

    vector<int> a(n);
    vector<int> b(m);

    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];
    
    vector<int> answer;


    int p1 = 0;
    int p2 = 0;

    while (p1 < n && p2 < m) {
        if (a[p1] < b[p2]) {
            answer.push_back(a[p1]);
            p1++;
        } else {
            answer.push_back(b[p2]);
            p2++;
        }
    }

    while (p1 < n) {
        answer.push_back(a[p1]);
        p1++;
    }

    while (p2 < m) {
        answer.push_back(b[p2]);
        p2++;
    }
    

    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i] << " ";
    }
}