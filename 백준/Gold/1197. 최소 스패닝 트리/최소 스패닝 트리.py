import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
parents = [i for i in range(v+1)]
edges = []

def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA == rootB:
        return True # cycle

    parents[rootB] = rootA
    return False
    

for _ in range(e):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[2])

edge_count = 0
answer = 0

for a, b, c in edges:
    if union(a, b):
        continue 
    else:
        answer += c
        edge_count += 1
        if edge_count == v - 1:
            print(answer)
            exit()