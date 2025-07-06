import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
rooms = []

for _ in range(n):
    s, e = map(int, input().rstrip().split(" "))
    rooms.append((s, e))

rooms.sort(key=lambda x: (-x[1])) # O(n log n)
reserved = [] # reserved 배열의 길이는 m으로 지정

for s, e in rooms: # O(n)
    if not len(reserved): 
        heapq.heappush(reserved, -s)
        continue

    _s = -heapq.heappop(reserved) # 현재 예약되어 있는 회의실 중 가장 빠른 시작 시간

    if e <= _s:
        heapq.heappush(reserved, -s)
    else:
        heapq.heappush(reserved, -_s)
        heapq.heappush(reserved, -s)

print(len(reserved))