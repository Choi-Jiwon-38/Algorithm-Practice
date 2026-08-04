from collections import deque

def solution(n, results):
    win = [[] for _ in range(n)]
    lose = [[] for _ in range(n)]
   
    for w, l in results:
        win[w - 1].append(l - 1)
        lose[l - 1].append(w - 1)
    
    
    def dfs(target, graph, visited):
        visited[target] = True
        count = 0 
        
        for next_target in graph[target]:
            if not visited[next_target]: 
                count += 1 + dfs(next_target, graph, visited)
        
        return count
        
    
    answer = 0
    
    for i in range(n):
        win_visited = [False for _ in range(n)]
        lose_visited = [False for _ in range(n)]
        
        win_count = dfs(i, win, win_visited)
        lose_count = dfs(i, lose, lose_visited)

        if win_count + lose_count + 1 == n:
            answer += 1
    
    return answer