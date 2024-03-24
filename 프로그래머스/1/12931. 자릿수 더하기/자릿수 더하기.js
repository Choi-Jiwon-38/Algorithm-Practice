function solution(n)
{
    let answer = 0;
    let num = n.toString();
    
    for (let i of num)
        answer += +i;
    
    return answer;
}