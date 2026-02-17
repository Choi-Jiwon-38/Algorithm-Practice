import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

c = int(input())
n = int(input())

networks = [[] for _ in range(c + 1)]
visited = [False for _ in range(c + 1)]

for _ in range(n):
    s, e = map(int, input().split())
    networks[s].append(e)
    networks[e].append(s)

answer = 0

dfs(networks, 1, visited)

for i in range(2, c + 1):
    if visited[i]: answer += 1

print(answer)