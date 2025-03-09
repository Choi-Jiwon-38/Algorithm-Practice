import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
hq = []

for _ in range(n):
    heapq.heappush(hq, int(input().rstrip()))

answer = 0

while len(hq) != 1:
    data1 = heapq.heappop(hq)
    data2 = heapq.heappop(hq)
    answer += data1 + data2
    heapq.heappush(hq, data1 + data2)

print(answer)