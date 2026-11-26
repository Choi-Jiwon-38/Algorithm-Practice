from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for __ in range(n)]
    
    s_pos = [None, None]
    e_pos = [None, None]
    l_pos = [None, None]
    
    dirs = [
        (0, 1),
        (0 , -1),
        (1, 0),
        (-1, 0)
    ]
    
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s_pos = [i, j]
            elif maps[i][j] == 'L':
                l_pos = [i, j]
            elif maps[i][j] == 'E':
                e_pos = [i, j]
    
    q = deque([(s_pos[0], s_pos[1], 0)])
    visited[s_pos[0]][s_pos[1]] = True
    
    l_dist = 0
    flag = True
    
    while q and flag:
        cy, cx, cd = q.popleft()
        
        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx
            nd = cd + 1
            
            if 0 <= ny and ny < n and 0 <= nx and nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                if ny == l_pos[0] and nx == l_pos[1]:
                    l_dist = nd
                    flag = False
                    break
                 
                visited[ny][nx] = True
                q.append((ny, nx, nd))
                

    # l_dist는 시작점 - 레버 거리    
    if l_dist == 0:
        return -1
    
    # 방문 배열 및 큐 초기화
    visited = [[False for _ in range(m)] for __ in range(n)]
    q = deque([(l_pos[0], l_pos[1], 0)])
    visited[l_pos[0]][l_pos[1]] = True

    e_dist = 0
    flag = True
    
    while q and flag:
        cy, cx, cd = q.popleft()
        
        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx
            nd = cd + 1
            
            if 0 <= ny and ny < n and 0 <= nx and nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                if ny == e_pos[0] and nx == e_pos[1]:
                    e_dist = nd
                    flag = False
                    break
                 
                visited[ny][nx] = True
                q.append((ny, nx, nd))
    
    if e_dist == 0:
        return -1
    
    return l_dist + e_dist