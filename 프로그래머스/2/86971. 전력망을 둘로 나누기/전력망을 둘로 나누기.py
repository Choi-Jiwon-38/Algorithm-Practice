def solution(n, wires):
    answer = 100
    
    graph = [[] for _ in range(n)]
    
    for s, e in wires:
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)
    
    def count_connected_node(node, visited):
        count = 1
        visited[node] = True
        
        for next_node in graph[node]:
            
            if not visited[next_node]:
                count += count_connected_node(next_node, visited)
        
        return count
    
    for s, e in wires:
        graph[s-1].remove(e-1)
        graph[e-1].remove(s-1)
        visited = [False] * n
    
        count1 = count_connected_node(0, visited)
        count2 = None
        
        for i in range(1, n):
            if not visited[i]:
                count2 = count_connected_node(i, visited)
                break
        
        diff = count1 - count2 if count1 > count2 else count2 - count1    
        answer = min(diff, answer)
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)
    
    
    return answer