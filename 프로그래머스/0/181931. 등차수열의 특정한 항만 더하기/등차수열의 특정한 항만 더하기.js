function solution(a, d, included) {
    let answer = 0;
    let num = a;
    
    for (let flag of included) {
        if (flag) {
            answer += num;
        }
        num += d;
    }
    
    return answer;
}