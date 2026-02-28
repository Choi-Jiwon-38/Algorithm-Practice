import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    u, v  = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

child_nodes = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
sizes = [None for _ in range(n+1)]

def makeTree(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            child_nodes[node].append(next_node) 
            makeTree(next_node)

def countSubTreeNodes(node):
    sizes[node] = 1
    for child_node in child_nodes[node]:
        countSubTreeNodes(child_node)
        sizes[node] += sizes[child_node]
 
makeTree(r)
countSubTreeNodes(r)

for _ in range(q):
    u = int(input())
    print(sizes[u])