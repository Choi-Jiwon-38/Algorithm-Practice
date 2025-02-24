import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(num, graph, visited):
    for next_node in graph[num]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, graph, visited)

n, m = map(int, input().rstrip().split(" "))

graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().rstrip().split(" "))
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

answer = 0

for i in range(n):
    if not visited[i]:
        answer += 1
        visited[i] = True
        dfs(i, graph, visited)

print(answer)