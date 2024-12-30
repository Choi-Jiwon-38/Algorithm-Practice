import sys
input = sys.stdin.readline

def dfs_find_distance(curr_node, target_node, graph, visit, dist = 0):
    if visit[curr_node]: # 이미 방문한 노드면 종료
        return False

    visit[curr_node] = True # 방문 처리

    for neighbor, weight in graph[curr_node]:
        if neighbor == target_node:
            print(dist + weight)
            return True
        else:
            dfs_find_distance(neighbor, target_node, graph, visit, dist + weight)

n, m = map(int, input().rstrip().split(" "))
graph = [[] for _ in range(n + 1)] # 1 ~ n까지 사용(0은 사용 X)

for _ in range(n - 1):
    start, end, dist = map(int, input().rstrip().split(" "))
    graph[start].append([end, dist])
    graph[end].append([start, dist])

for _ in range(m):
    visit = [False for _ in range(n + 1)]
    node1, node2 = map(int, input().rstrip().split(" "))
    dfs_find_distance(node1, node2, graph, visit)