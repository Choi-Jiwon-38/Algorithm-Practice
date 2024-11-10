#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long n, m;
    long long answer = 0;

    cin >> n >> m;

    vector<long long> M(n + 1, 0);
    vector<long long> R(m, 0);

    for (int i = 1; i <= n; i++) {
        long long tmp;
        cin >> tmp;
        // 구간합 배열
        M[i] = M[i-1] + tmp;
    }

    for (int i = 1; i <= n; i++) {
        int remain = M[i] % m;

        if (remain == 0) answer++;

        R[remain]++;
    }

    for (int i = 0; i < m; i++) {
        if (R[i] > 1)
            answer += R[i] * (R[i] - 1) / 2;
    }


    cout << answer;
}