// 백준 온라인 저지 15727번
#include <iostream>
using namespace std;

int main(void) {
    int num;
    int answer = 0;
    cin >> num;
    answer += num / 5;
    if (num % 5 != 0) {
        answer += 1;
    }
    cout << answer << endl;
}
