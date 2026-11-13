def dfs(n, graph, node, visited):
    for i in range(n):
        if graph[node][i] and not visited[i]:
            visited[i] = True
            dfs(n, graph, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = True
            dfs(n, computers, i, visited)

    return answer