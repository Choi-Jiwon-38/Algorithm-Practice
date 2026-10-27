from collections import deque

dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

def solution(maps):
    answer = -1
    q = deque([(0, 0, 1)])
    n = len(maps)
    m = len(maps[0])
    
    maps[0][0] = -1
    
    while len(q):
        cy, cx, cc = q.popleft()
        
        if cy == n - 1 and cx == m - 1:
            answer = cc
            break
        
        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx
            nc = cc + 1
            
            if 0 <= ny and ny < n and 0 <= nx and nx < m and maps[ny][nx] == 1:
                maps[ny][nx] = -1
                q.append((ny, nx, nc))
    
    return answer