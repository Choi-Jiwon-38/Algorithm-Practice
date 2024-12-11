#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<int> v(n+1);

    // base case
    v[0] = 1;
    v[1] = 1; // 세로 1개
    v[2] = 2; // 가로 2개 or 세로 2개


    // recursive case
    for (int i = 3; i <= n; i++)
        v[i] = (v[i - 1] + v[i - 2]) % 10007 ;
    
    cout << v[n]<< '\n';
}