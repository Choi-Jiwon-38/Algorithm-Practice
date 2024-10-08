#include <iostream>
using namespace std;
int main() {
    int A, B, V;
    cin >> A >> B >> V;
    
    int answer = 1;

    if (A < V) {
        answer += (V - A) / (A - B);

        if ((V - A) % (A - B) != 0)
            answer++;
    }
    cout <<  answer << endl;    

}
