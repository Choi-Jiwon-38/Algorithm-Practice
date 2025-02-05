import sys
import heapq
input = sys.stdin.readline

graph = []
indegree = []

n, m = map(int, input().rstrip().split(" "))

# O(n)
for _ in range(n):
    graph.append([])
    indegree.append(0)

# O(m)
for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))    
    graph[a - 1].append(b - 1)
    indegree[b - 1] += 1

answer = []
hq = []

# O(n * log n)
for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(hq, i) # O(log n)

# O((n + m) * log n)
while len(hq):
    node = heapq.heappop(hq)
    answer.append(node + 1) # O(log n)
    
    for next_node in graph[node]: # O('출발 노드의 간선 개수')
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            heapq.heappush(hq, next_node) # O(log n)

print(*answer)

# n <= 32,000 | m <= 100,000
# 최종 시간복잡도는 132,000 * log 32,000 에 해당함.