function solution(answers) {
    let answer = [];
    let score1 = 0;
    let score2 = 0;
    let score3 = 0;
    
    const sol1 = [1,2,3,4,5];
    const sol2 = [2,1,2,3,2,4,2,5];
    const sol3 = [3,3,1,1,2,2,4,4,5,5];
    
    for (var i = 0; i < answers.length; i++) {
        if (answers[i] === sol1[i % sol1.length])
            score1++;
        if (answers[i] === sol2[i % sol2.length])
            score2++;
        if (answers[i] === sol3[i % sol3.length])
            score3++
    }
    
    const maxScore = Math.max(score1, score2, score3);
    
    if (score1 === maxScore)
        answer.push(1);
    if (score2 === maxScore)
        answer.push(2);
    if (score3 === maxScore)
        answer.push(3);   
    
    return answer;
}