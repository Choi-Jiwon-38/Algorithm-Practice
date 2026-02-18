import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True

    while len(q):
        x = q.popleft()
        print(x, end=" ")

        for next in graph[x]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


n, m, v  = map(int, input().split())
graph = [[] for _ in range(n + 1)] # graph[0]은 미사용

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False for _ in range(n + 1)]
dfs(graph, v, visited)
print()
visited = [False for _ in range(n + 1)]
bfs(graph, v, visited)