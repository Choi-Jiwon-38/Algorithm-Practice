#include <iostream>

using namespace std;
// 2중 for문을 통하여 풀이하는 경우에는 O(n^2)
// two pointer 알고리즘을 통하여 풀이하는 경우에는 O(2n) -> O(N)으로 풀이 가능

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    while (1) {
        int n, m;
        cin >> n >> m;

        if (n == 0 && m == 0)
            break;

        int arr1[n];
        int arr2[m];

        for (int i = 0; i < n; i++) cin >> arr1[i];
        for (int i = 0; i < m; i++) cin >> arr2[i];
        
        int i = 0;
        int j = 0;

        int answer = 0;

        while (i < n && j < m) {
            if (arr1[i] == arr2[j]) {
                i++; j++;
                answer++;
            } else {
                if (arr1[i] < arr2[j]) {
                    i++;
                } else { // arr1[i] > arr2[j]
                    j++;
                }
            }
        }
        cout << answer << '\n';
    }

}