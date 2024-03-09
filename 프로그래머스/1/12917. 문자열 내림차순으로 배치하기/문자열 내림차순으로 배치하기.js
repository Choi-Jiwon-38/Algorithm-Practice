

function solution(s) {
    let array = [];
    let answer = '';
    
    for (let str of s) {
        array.push(str);
    }
    
    array.sort();
    array.reverse();
    
    for (let str of array) {
        answer += str;
    }
    
    // var answer = s;
    return answer;
}