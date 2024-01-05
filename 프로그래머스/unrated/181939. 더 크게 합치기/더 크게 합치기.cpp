#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    string str_a = to_string(a);
    string str_b = to_string(b);
    
    return (str_a + str_b > str_b + str_a) ? stoi(str_a + str_b) : stoi(str_b + str_a);
}