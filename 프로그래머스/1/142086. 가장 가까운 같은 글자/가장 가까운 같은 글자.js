function solution(s) {
    let words = new Map();
    let answer = [];    
    let len = s.length;
    for (let i = 0; i < len; i++) {
        let result = words.get(s[i]);
        if (result === undefined) {
            answer.push(-1);
        } else {
            answer.push(i - result);
        }
        words.set(s[i], i);
    }    

    return answer;
}