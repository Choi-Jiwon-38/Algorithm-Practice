import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split(" "))

q = deque([])

min_time = -1 # 없음을 의미
min_time_count = 0

dist = [200000 for _ in range(100001)]

def valid(num):
    if num < 0 or num > 100000:
        return False
    return True

def bfs():
    global min_time, min_time_count # 전역 변수로 선언
    while len(q):
        loc, time = q.popleft()

        if dist[loc] < time:
            continue

        dist[loc] = time

        if min_time > -1:
            if min_time < time:
                break

        if loc == k:
            if min_time == -1:  # 처음 도달한 경우
                min_time = time
            min_time_count += 1
        
        if valid(loc - 1):
            q.append([loc - 1, time + 1])
        
        if valid(loc + 1):
            q.append([loc + 1, time + 1])

        if valid(loc * 2):
            q.append([loc * 2, time + 1])

q.append([n, 0])
bfs()

print(min_time)
print(min_time_count)