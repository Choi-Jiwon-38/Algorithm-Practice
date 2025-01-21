import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())

trees = [[] for _ in range(n)]

for _ in range(n - 1):
    node1, node2 = map(int, input().rstrip().split(" "))
    trees[node1 - 1].append(node2)
    trees[node2 - 1].append(node1)

parents = [-1 for _ in range(n)]
visit = [False for _ in range(n)]

def dfs(curr_node, from_node):
    if visit[curr_node - 1]: # 이미 방문한 노드인 경우
        return False
    
    visit[curr_node - 1] = True # 방문 처리
    parents[curr_node - 1] = from_node # 부모 노드 추가

    for node in trees[curr_node - 1]:
        dfs(node, curr_node)

dfs(1, 1)

for i in range(1, n):
    print(parents[i])
