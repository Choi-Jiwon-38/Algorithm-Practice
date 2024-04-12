function solution(n) {
    let tNum = n.toString(3).split("");
    let rtNum = tNum.reverse();
    
    let rtStr = '';
    for (let num of rtNum) {
        rtStr += num;
    }
    
    let answer = +(parseInt(rtStr,3)).toString(10);
    return answer;
}