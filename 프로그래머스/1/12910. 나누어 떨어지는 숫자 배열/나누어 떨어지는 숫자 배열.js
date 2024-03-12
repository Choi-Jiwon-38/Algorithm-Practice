function solution(arr, divisor) {
    let answer = [];
    
    for (let a of arr) {
        if (a % divisor === 0)
            answer.push(a);
    }
    
    answer.sort(function(a,b) {
        return a-b;
    });
    
    if (answer.length === 0)
        answer.push(-1);
    
    return answer;
}