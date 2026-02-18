import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    c1, c2 = map(int, input().split())
    graph[c2].append(c1)

visited = [0 for _ in range(n + 1)]
visit_id = 0

def bfs(graph, v, visited):
    global visit_id
    visit_id += 1
    q = deque([v])
    visited[v] = visit_id
    count = 1

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if visited[nx] != visit_id:
                visited[nx] = visit_id
                count += 1
                q.append(nx)

    return count

max_count = 0
answer = []

for i in range(1, n + 1):
    count = bfs(graph, i, visited)

    if max_count == count:
        answer.append(i)
    elif max_count < count:
        max_count = count
        answer = [i]

print(*answer)