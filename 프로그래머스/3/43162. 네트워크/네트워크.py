def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(index):
        nonlocal visited
        visited[index] = True     
        
        for i in range(n):
            if computers[index][i] == 1 and not visited[i]:
                visited[i] = True
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
        
    return answer