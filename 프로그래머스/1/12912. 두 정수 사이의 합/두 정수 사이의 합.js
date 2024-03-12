function solution(a, b) {
    if (a === b) // a와 b가 같은 경우
        return a;
    
    let answer = 0;
    
    if (a > b) {
        for (let i = b; i <= a; i++)
            answer += i;
        return answer;
    }
    if (a < b) {
        for (let i = a; i <= b; i++)
            answer += i;
        return answer;
    }

}