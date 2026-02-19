import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())

maps = []
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    maps.append(list(map(int, input().split())))

# bfs
cy, cx, hasGram, step = 0, 0, 0, 0

q = deque([(cy, cx, hasGram, step)])
visited[cy][cx][0] = step

answer = 'Fail'

while q:
    if answer != 'Fail': break
    y, x, hasGram, step = q.popleft()
    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        nStep = step + 1

        if ny == n - 1 and nx == m - 1:
            answer = nStep
            break

        if ny < 0 or ny >= n or nx < 0 or nx >= m: # boundary check
            continue

        if maps[ny][nx] == 1 and hasGram and not visited[ny][nx][hasGram]:
            visited[ny][nx][hasGram] = True
            if nStep <= t: q.append((ny, nx, hasGram, nStep))
        elif maps[ny][nx] == 2 and not visited[ny][nx][1]:
            visited[ny][nx][1] = True
            if nStep <= t: q.append((ny, nx, 1, nStep))
        elif maps[ny][nx] == 0 and not visited[ny][nx][hasGram]:
            visited[ny][nx][hasGram] = True
            if nStep <= t: q.append((ny, nx, hasGram, nStep))
            
print(answer)