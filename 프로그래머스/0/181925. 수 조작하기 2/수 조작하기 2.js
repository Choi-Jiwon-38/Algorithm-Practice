function solution(numLog) {
    let answer = '';
    let num;
    
    for (let i = 1; i < numLog.length; i++) {
        num = numLog[i] - numLog[i-1];
        
        switch(num) {
            case 1:
                answer += 'w';
                break;
            case -1:
                answer += 's';
                break;
            case 10:
                answer += 'd';
                break;
            case -10:
                answer += 'a';
                break;
        }
    }
    
    
    
    return answer;
}