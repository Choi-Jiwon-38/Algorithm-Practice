#include <iostream>
#include <string>

using namespace std;

int main()
{
    bool isMinus = false;
    string input, num;
    int answer = 0;
    cin >> input;

    for (char c : input)
    {
        if (c == '-' || c == '+')
        {
            isMinus ? answer -= stoi(num) : answer += stoi(num);
            num = "";
            if (c == '-')
                isMinus = true;
        }
        else
        {
            num += c;
        }
    }
    isMinus ? answer -= stoi(num) : answer += stoi(num); // 마지막 수
    cout << answer;
}