function solution(t, p) {
    let answer = 0;
    let pLen = p.length;
    let loopLimit = t.length - pLen + 1;
    for (let i = 0; i < loopLimit; i++) {
        if (+t.slice(i, i + pLen) <= +p)
                answer++;
        }
    return answer;
}