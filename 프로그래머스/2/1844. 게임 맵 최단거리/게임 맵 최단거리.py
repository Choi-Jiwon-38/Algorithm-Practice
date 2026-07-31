from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dq = deque([(0, 0, 1)])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while dq:
        cy, cx, step = dq.popleft()
        
        if cy == n - 1 and cx == m - 1:
            return step
        
        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx
    
            if 0 <= ny and ny < n and 0 <= nx and nx < m and maps[ny][nx] == 1 and not visited[ny][nx]:
                dq.append((ny, nx, step + 1))
                visited[ny][nx] = True
    
    return -1