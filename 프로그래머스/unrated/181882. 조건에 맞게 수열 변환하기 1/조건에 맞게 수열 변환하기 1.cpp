#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    for (int x : arr)
    {
        if (x >= 50 && x % 2 == 0)
            answer.push_back(x / 2);
        else if (x < 50 && x % 2 != 0)
            answer.push_back(x * 2);
        else
            answer.push_back(x);
    }
    return answer;
}