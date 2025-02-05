import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))

graph = []
indegrees = []

for i in range(n):
    graph.append([])
    indegrees.append(0)

for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))
    graph[a - 1].append(b - 1)
    indegrees[b - 1] += 1

dq = deque([])

for i in range(n):
    if indegrees[i] == 0:
        dq.append(i)

result = []

while len(dq):
    node = dq.popleft()
    result.append(node + 1)
    
    for next_node in graph[node]:
        indegrees[next_node] -= 1
        if indegrees[next_node] == 0:
            dq.append(next_node)

print(*result)