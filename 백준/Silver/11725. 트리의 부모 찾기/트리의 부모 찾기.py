import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [None for _ in range(n+1)]

for i in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph, v, parents):
    q = deque([v])

    while len(q):
        x = q.popleft()
        
        for nx in graph[x]:
            if parents[nx] is None:
                parents[nx] = x
                q.append(nx)

bfs(graph, 1, parents)

for i in range(2, n+1):
    print(parents[i])