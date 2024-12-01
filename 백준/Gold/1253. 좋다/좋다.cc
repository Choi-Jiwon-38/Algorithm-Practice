#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int answer = 0; 
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr, arr + n);


    for (int i = 0; i < n; i++) {
        int l = 0;
        int r = n - 1;
        long target = arr[i];

        while (l < r) {
            int s = arr[l] + arr[r];
            if (s == target) {
                if (r != i && l != i) {
                    answer++;
                    break;
                } else if (l == i) {
                    l++;
                } else if (r == i) {
                    r--;
                }
            } else if (s < target) {
                l++;
            } else { // s > target
                r--;
            }
        }
    }
    cout << answer << '\n';
}
