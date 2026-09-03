function solution(n, computers) {
    const visited = Array(n).fill(false);
    let answer = 0;
    
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            answer++;
            dfs(i);
        }
    }
        
        
    function dfs(node) {
        const computer = computers[node];
        
        for (let i = 0; i < n; i++) {
            if (!visited[i] && computer[i] == 1) {
                visited[i] = true;
                dfs(i);
            }
        }
        
    }
    
    return answer;
}