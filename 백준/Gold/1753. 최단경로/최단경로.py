import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().rstrip().split(" ")) # 정점 개수, 간선 개수
K = int(input().rstrip()) # 시작 정점 번호

graph = {}

for _ in range(E):
    u, v, w = map(int, input().rstrip().split(" "))
    
    if u in graph:
        graph[u].append([v, w])
    else:
        graph[u] = [[v, w]]

dist = ['INF' for _ in range(V + 1)]
dist[K] = 0
hq = [(0, K)]

def dijkstra():
    while hq:
        current_dist, current_node = heapq.heappop(hq)
        if dist[current_node] != 'INF' and current_dist > dist[current_node]:
            continue

        if current_node in graph:
            for neighbor, weight in graph[current_node]:
                new_dist = current_dist + weight
                if dist[neighbor] == 'INF' or new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(hq, (new_dist, neighbor))

dijkstra()

for i in range(1, V + 1):
    print(dist[i])

