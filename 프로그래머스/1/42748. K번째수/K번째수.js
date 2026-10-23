function solution(array, commands) {
    const answer = [];
    
    for (const cmd of commands) {
        let i = cmd[0]
        let j = cmd[1]
        let k = cmd[2]
        
        result = array.slice(i - 1, j).sort((a, b) => a - b)
        
        answer.push(result[k - 1])
    }

    return answer;
}