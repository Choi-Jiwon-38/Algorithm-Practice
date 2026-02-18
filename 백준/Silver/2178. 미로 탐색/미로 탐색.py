import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(n):
    maps.append(list(map(int, input().rstrip())))

def bfs(sy, sx):
    q = deque([(sy, sx, 1)])
    maps[sy][sx] = 0 # visit check

    while q:
        y, x, dir = q.popleft()
        
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            ndir = dir + 1

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
                
            if maps[ny][nx] == 1:
                if ny == n - 1 and nx == m - 1: # end
                    print(ndir)
                    exit()

                maps[ny][nx] = 0
                q.append((ny, nx, ndir))

bfs(0, 0)