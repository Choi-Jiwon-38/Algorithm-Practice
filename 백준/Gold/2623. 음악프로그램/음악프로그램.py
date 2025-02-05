import sys
input = sys.stdin.readline
from collections import deque

graph = []
indegree = []


n, m = map(int, input().rstrip().split(" "))

for i in range(n):
    graph.append([])
    indegree.append(0)




for i in range(m):
    orders = list(map(int, input().rstrip().split(" ")))
    num_of_singer = orders[0]

    for i in range(1, num_of_singer):
        curr_node, next_node = orders[i] - 1, orders[i+1] - 1

        graph[curr_node].append(next_node)
        indegree[next_node] += 1

q = deque([])

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

answer = []

while len(q):
    node = q.popleft()
    answer.append(node + 1)

    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)


if len(answer) != n:
    print(0)
else:
    for node in answer:
        print(node)