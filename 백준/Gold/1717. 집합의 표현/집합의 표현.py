import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
    
def find(a, parents):
    if a != parents[a]:
        parents[a] = find(parents[a], parents)
    return parents[a]
    
def union(a, b, parents):
    a_parents = find(a, parents)
    b_parents = find(b, parents)
    
    if a_parents < b_parents:
        parents[b_parents] = a_parents
    else:
        parents[a_parents] = b_parents

n, m = map(int, input().rstrip().split(" "))
parents = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().rstrip().split(" "))
    
    if cmd == 0:
        union(a, b, parents)
    else:
        print("YES" if find(a, parents) == find(b, parents) else "NO")