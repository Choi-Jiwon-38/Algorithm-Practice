from collections import deque

def find(n, parent):
    if parent[n] != n:
        parent[n] = find(parent[n], parent)
        
    return parent[n]

def union(n1, n2, parent):
    p1 = find(n1, parent)
    p2 = find(n2, parent)
    
    parent[p2] = p1

def solution(n, costs):
    edge_with_weight = []
    edge_count = 0
    
    for node1, node2, cost in costs:
        edge_with_weight.append((cost, (node1, node2)))
    
    q = deque(sorted(edge_with_weight))
                                
    answer = 0
    parent = [i for i in range(n + 1)]
    
    while edge_count < n - 1:
        cost, (node1, node2) = q.popleft()
        
        if find(node1, parent) == find(node2, parent):
            # 사이클이 생성된 경우
            pass
        else:
            union(node1, node2, parent)
            answer += cost
            edge_count += 1
                                
    return answer