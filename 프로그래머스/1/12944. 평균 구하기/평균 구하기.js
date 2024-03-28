function solution(arr) {
    var answer = 0;
    
    for (let a of arr) {
        answer += a;
    }
    
    return answer / arr.length;
}