function solution(s) {
    var answer = [0, 0];
    let oldLen, newLen;
    
    while (s !== "1") {
        oldLen = s.length;
        s = s.replaceAll('0', '');
        newLen = s.length;
        s = (s.length).toString(2);
        answer[0]++;
        answer[1] += oldLen - newLen;
    }

    return answer;
}