#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    int arr[n];
    
    for (int i = 0; i < n; i++) cin >> arr[i];

    sort(arr, arr + n);

    int l = 0;
    int r = n - 1;

    int answer = 0;

    while (l < r) {
        int s = arr[r] + arr[l];
        
        if (s > m) {
            r--;
        } else if (s < m) {
            l++; 
        } else {
            l++;
            r--;
            answer++;
        }
    }

    cout << answer << '\n';
}
