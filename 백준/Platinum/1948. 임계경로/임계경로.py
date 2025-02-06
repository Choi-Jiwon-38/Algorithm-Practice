import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = []
indegree = []

for _ in range(n):
    graph.append([])
    indegree.append(0)

for i in range(m):
    s, e, w = map(int, input().rstrip().split(" "))
    graph[s - 1].append((e - 1, w)) # (노드 번호, 가중치)
    indegree[e - 1] += 1

s, e = map(int, input().rstrip().split(" "))

time = [0] * n
cnt = [[] for _ in range(n)]

q = deque([s - 1])

while len(q):
    node = q.popleft()

    for next_node, next_time in graph[node]:
        indegree[next_node] -= 1

        if time[next_node] < time[node] + next_time:
            time[next_node] = time[node] + next_time
            cnt[next_node] = [node]
        elif time[next_node] == time[node] + next_time:
            cnt[next_node].append(node)

        if indegree[next_node] == 0:
            q.append(next_node)

q_path = deque([e - 1])
path = set()

while len(q_path):
    node = q_path.popleft()
    for prev_node in cnt[node]:
        if (prev_node, node) not in path:
            path.add((prev_node, node))
            q_path.append(prev_node)

print(time[e - 1])
print(len(path))





