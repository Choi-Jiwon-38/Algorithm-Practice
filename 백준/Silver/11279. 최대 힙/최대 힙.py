import sys
import heapq

input = sys.stdin.readline
max_heap = []

x = int(input().rstrip())

for _ in range(x):
    num = int(input().rstrip())
    
    if num == 0:
        print(-heapq.heappop(max_heap) if len(max_heap) else 0)
    else:
        heapq.heappush(max_heap, -num)