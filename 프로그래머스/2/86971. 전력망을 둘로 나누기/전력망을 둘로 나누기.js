
function dfs(graph, i, visited) {
    for (const nextNode of graph[i]) {
        if (visited[nextNode] === false) {
            visited[nextNode] = true;
            dfs(graph, nextNode, visited);
        }
    }
}

function make_network(wires, n, skipIndex) {
    const graph = Array.from({ length: n}, () => []);
    const visited = Array(n).fill(false);
    
    for (let i = 0; i < wires.length; i++) {
        if (i === skipIndex) continue;
        
        let s = wires[i][0];
        let e = wires[i][1];
        
        graph[s - 1].push(e - 1);
        graph[e - 1].push(s - 1); 
    }
    
    visited[0] = true;
    dfs(graph, 0, visited);
    
    const count = visited.filter(x => x).length;
    return  Math.abs(n - 2 * count)
}

function solution(n, wires) {
    let answer = 100;
    
    for (let i = 0; i < n; i++) {
        answer = Math.min(make_network(wires, n, i), answer);
    }
    
    return answer;
}
