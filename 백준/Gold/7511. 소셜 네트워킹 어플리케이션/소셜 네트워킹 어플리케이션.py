import sys
input = sys.stdin.readline

t = int(input().rstrip())


def find(x, parents):
    if parents[x] != x:
        return find(parents[x], parents)
    return x

def union(a, b, parents):
    a_parent = find(a, parents)
    b_parent = find(b, parents)

    if a_parent > b_parent:
        parents[a_parent] = b_parent 
    else:
        parents[b_parent] = a_parent


for i in range(1, t + 1):
    print(f"Scenario {i}:")
    n = int(input().rstrip()) # 유저의 수
    
    parents = [index for index in range(n)] # union find를 위한 배열

    k = int(input().rstrip()) # 친구 관계의 수

    for _ in range(k):
        a, b = map(int, input().rstrip().split(" "))
        union(a, b, parents) 

    m = int(input().rstrip()) # 구할 쌍의 수

    for _ in range(m):
        u, v = map(int, input().rstrip().split(" "))
        print(1 if find(u, parents) == find(v, parents) else 0) 
    
    print('')
