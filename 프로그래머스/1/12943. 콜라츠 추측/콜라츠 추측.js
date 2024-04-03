function solution(num) {
    var answer = 0;
    
    while (num > 1) {
        (num % 2 === 0) ? num /= 2 : num = num * 3 + 1;
        answer++;
        if(answer === 500) {
            return -1;
        }
    }
    return answer;
}