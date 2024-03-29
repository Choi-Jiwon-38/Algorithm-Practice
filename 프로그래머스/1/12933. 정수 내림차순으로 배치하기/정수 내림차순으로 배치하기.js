function solution(n) {
    n = n.toString();
    
    let arr = [];
    
    for (let i of n) {
        arr.push(+i);
    }
    
    arr.sort((a, b) => b - a);
    
    var answer = "";
    
    for (let a of arr) {
        answer += a;
    }
    
    return +answer;
}