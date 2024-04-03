function findMeasure(n) {
    let measure = 0;
    let sqrtN = Math.sqrt(n);
    
    for (let i = 1; i <= sqrtN; i++) {
        if (n % i === 0) {
            (i === sqrtN) ? measure++ : measure += 2;
        }
    }
    console.log(n, measure % 2 === 0, measure);
    
    return measure % 2 === 0;
    
}

function solution(left, right) {
    var answer = 0;
    
    for (let i = left; i <= right; i++) {
        const result = findMeasure(i);
        result ? answer += i  : answer -= i; 
    }
    
    
    return answer;
}