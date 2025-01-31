import sys
from collections import deque
input = sys.stdin.readline

snake = {}
ledder = {}

n, m = map(int, input().rstrip().split(" "))

for _ in range(n):
    start, end = map(int, input().rstrip().split(" "))
    ledder[start] = end

for _ in range(m):
    start, end = map(int, input().rstrip().split(" "))
    snake[start] = end

q = deque([(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]) # (현재 칸, 주사위 굴린 횟수)

visit = set([2, 3, 4, 5, 6, 7])
while len(q):
    curr, roll_count = q.popleft()

    if curr == 100:
        print(roll_count)
        break

    if curr in ledder:
        curr = ledder[curr]
    
    if curr in snake:
        curr = snake[curr]
    
    for i in range(1, 7):
        if curr + i not in visit and curr + i <= 100:
            q.append((curr + i, roll_count + 1))
            visit.add(curr + i)
