from collections import deque

MAX_SIZE = 51

def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
    visited = [[False for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
    
    for sx, sy, ex, ey in rectangle:
        for i in range(sx, ex + 1):
            maps[sy][i] = 1
            maps[ey][i] = 1
        
        for i in range(sy, ey + 1):
            maps[i][sx] = 1
            maps[i][ex] = 1
            
    dq = deque([(characterY, characterX, 0)])  
    visited[characterY][characterX] = True
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def isEdge(y, x, sy, sx, ey, ex):
        return ((x == sx or x == ex) and (sy <= y and y <= ey)) or ((y == sy or y == ey) and (sx <= x and x <= ex))
        
    def isIncluded(y, x, sy, sx, ey, ex):
        return sx < x and x < ex and sy < y and y < ey
    
    while (dq):
        cy, cx, step = dq.popleft()
        print(cx, cy, step)
        
        if cy == itemY and cx == itemX:
            return step
        
        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx
            
            if ny > 0 and ny < MAX_SIZE and nx > 0 and nx < MAX_SIZE and maps[ny][nx] == 1 and not visited[ny][nx]: # 갈 수 있는 경우
                included = False
                isSameRect = False
                
                for sx, sy, ex, ey in rectangle:
                    if isEdge(cy, cx, sy, sx, ey, ex) and isEdge(ny, nx, sy, sx, ey, ex):
                        if (cx == nx and (nx == sx or nx == ex) and sy <= cy and cy <= ey and sy <= ny and ny <= ey) or (cy == ny and (ny == sy or ny == ey) and sx <= cx and cx <= ex and sx <= nx and nx <= ex):
                        
                            isSameRect = True
                    
                    if isIncluded((ny + cy) / 2, (nx + cx) / 2, sy, sx, ey, ex):
                        included = True
                
                if not included and isSameRect:
                    visited[ny][nx] = True
                    dq.append((ny, nx, step + 1))
                    
        
                
                