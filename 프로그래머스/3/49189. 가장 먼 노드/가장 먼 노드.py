from collections import deque

def solution(n, edge):
    max_dist = 0
    answer = 0
    
    visited = [False for _ in range(n)]
    graph = [[] for _ in range(n)]
    
    for node1, node2 in edge:
        graph[node1 - 1].append(node2 - 1)
        graph[node2 - 1].append(node1 - 1)
    
    
    visited[0] = True
    q = deque([(0, 0)])
    
    while q:    
        curr_node, curr_dist = q.popleft()
        
        if max_dist == curr_dist:
            answer += 1
        elif max_dist < curr_dist:
            max_dist = curr_dist
            answer = 1
        
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, curr_dist + 1))            
        
    
    return answer