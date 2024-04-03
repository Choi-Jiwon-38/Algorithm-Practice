function solution(n) {
    var answer = '';
    
    if (n % 2 === 0) {
        answer += "수박".repeat(n / 2);
    } else {
        answer += "수박".repeat((n - 1) / 2);
        answer += "수"
    }
    
    return answer;
}