from collections import deque

def solution(n, edge):
    graph = dict()
    dist = dict() # dist가 -1이면 미방문을 의미
    
    for n1, n2 in edge:
        dist[n1] = dist[n2] = -1
    
        if n1 in graph:
            graph[n1].append(n2)
        else:
            graph[n1] = [n2]
            
        if n2 in graph:
            graph[n2].append(n1)
        else:
            graph[n2] = [n1]
    
    dq = deque([1])
    dist[1] = 0

    while (dq):
        node = dq.popleft()
        d = dist[node]
        
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = d + 1
                dq.append(next_node)
    
    max_dist = max(dist.values())
    answer = 0
    
    for d in dist.values():
        if max_dist == d:
            answer += 1
    
    
    return answer