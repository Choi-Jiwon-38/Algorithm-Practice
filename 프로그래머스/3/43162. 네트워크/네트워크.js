
function solution(n, computers) {
    function dfs(n, currNode, computers) {        
        for (let i = 0; i < n; i++) {
            if (computers[currNode][i] === 1 && visited[i] === false) {
                visited[i] = true;
                dfs(n, i, computers, visited);
            }               
        }
    }
    
    const visited = Array(n).fill(false);
    var answer = 0;
    
    for (let i = 0; i < n; i++) {
        if (visited[i] === false) {
            visited[i] = true;
            dfs(n, i, computers);
            answer++;
        }
    }
    
    return answer;
    


}

