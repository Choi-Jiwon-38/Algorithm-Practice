from collections import deque

answer = 100

def travel(n, graph, visited):    
    global answer
    dq = deque([0])
    visited[0] = True
    
    while dq:
        node = dq.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dq.append(next_node)
    
    count1 = visited.count(True)
    count2 = n - count1

    answer = min(answer, abs(count1 - count2)) 
    
    

def make_graph(wires, index, n):
    graph = [[] for _ in range(n)] 
    
    for i in range(len(wires)):
        if i == index:
            continue
        
        node1, node2 = wires[i]
    
        graph[node1 - 1].append(node2 - 1)
        graph[node2 - 1].append(node1 - 1)
    
    return graph
        

def solution(n, wires):
    for i in range(len(wires)):
        visited = [False for _ in range(n)]
        graph = make_graph(wires, i, n)
        travel(n, graph, visited)
    
    return answer