function solution(n)
{
    let num = n;
    let answer = 1;
    
    while (num !== 1) {
        if (num % 2 === 0) {
            num = num / 2;
        } else {
            answer++;
            num = parseInt(num / 2);
        }
    }
    
    
    return answer;
}