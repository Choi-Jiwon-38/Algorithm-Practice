#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;

    cin >> n;

    int start = 1;
    int end = 1;
    int answer = 1;
    int sum = 1;

    while (end != n) {
        if (sum == n) {
            answer++;
            end++;
            sum += end;
        } else if (sum < n) {
            end++;
            sum += end;
        } else if (sum > n) {
            sum -= start;
            start++;
        }
    }
    cout << answer << '\n';
}
