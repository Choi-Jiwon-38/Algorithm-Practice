import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[None] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = [[None] * m for _ in range(n)]

s = None

for i in range(n):
    r = list(map(int, input().split()))
    
    for j in range(m):
        maps[i][j] = r[j]
        if r[j] == 2:
            s = (i, j)


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(y, x):
    q = deque([(y, x, 0)])
    visited[y][x] = True
    answer[y][x] = 0

    while q:
        y, x, dist = q.popleft()
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            nd = dist + 1

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            else:
                if (not visited[ny][nx]) and maps[ny][nx] != 0:
                    visited[ny][nx] = True
                    q.append((ny, nx, nd))
                    answer[ny][nx] = nd

bfs(s[0], s[1])

for i in range(n):
    for j in range(m):
        if answer[i][j] is None:
            if maps[i][j] == 0:
                answer[i][j] = 0
            else:
                answer[i][j] = -1

for i in range(n):
    print(*answer[i])