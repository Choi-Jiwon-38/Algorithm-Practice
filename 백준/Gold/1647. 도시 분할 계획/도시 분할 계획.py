import sys
input = sys.stdin.readline

n, m = map(int, input().split())
 
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    parent[rootB] = rootA

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, (a, b)))

edges.sort()
answer = 0
edge_count = 0

max_selected_edge_weight = 0

for c, (a, b) in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c
        max_selected_edge_weight = max(max_selected_edge_weight, c)
        edge_count += 1

        if edge_count == n - 1:
            break

answer -= max_selected_edge_weight

print(answer)