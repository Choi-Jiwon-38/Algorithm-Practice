import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, k = map(int, input().rstrip().split(" "))
    costs = list(map(int, input().rstrip().split(" ")))
    indegree = []
    graph = []
    pending = []
    
    
    for _ in range(n):
        indegree.append(0)
        graph.append([])
        pending.append(0)
    
    for _ in range(k):
        x, y = map(int, input().rstrip().split(" "))
        x -= 1
        y -= 1
        
        graph[x].append(y)
        indegree[y] += 1
    
    w = int(input().rstrip())
    w -= 1
    
    q = deque([])
    
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    while len(q):
        node = q.popleft()
        curr_time = pending[node] + costs[node]
        
        if node == w:
            print(curr_time)
            break
        
        for next_node in graph[node]:
            indegree[next_node] -= 1
            pending[next_node] = max(pending[next_node], curr_time)
            if indegree[next_node] == 0:
                q.append(next_node)