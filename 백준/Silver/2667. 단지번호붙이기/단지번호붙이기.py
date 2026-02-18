import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
total = 0

maps = []
answer = []

for _ in range(n):
    maps.append(list(map(int, input().rstrip())))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(sy, sx):
    global total
    total += 1
    count = 1
    maps[sy][sx]= 0 # visit check


    q = deque([(sy, sx)])

    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx

            # boundary check
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
                
            if maps[ny][nx] == 1:
                maps[ny][nx] = 0
                count += 1
                q.append((ny, nx))

    return count            

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            count = bfs(i, j)
            answer.append(count)

answer.sort()


print(total)

for a in answer:
    print(a)