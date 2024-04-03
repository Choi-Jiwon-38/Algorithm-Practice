function solution(s) {
    var answer = '';
    let flag = true;
    
    for (let c of s) {
        if (c === " ") {
            flag = true;
            answer += c;
            continue;
        }
        
        if (flag) {
            answer += c.toUpperCase();
            flag = false;
        } else {
            answer += c.toLowerCase()
        }  
    }
    
    return answer;
}