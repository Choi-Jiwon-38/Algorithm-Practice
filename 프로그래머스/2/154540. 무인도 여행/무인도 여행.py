import sys

sys.setrecursionlimit(10**6)

dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def calculate_days(y, x, n, m, visited, maps):
    days = int(maps[y][x])
    
    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and maps[ny][nx] != 'X':
            visited[ny][nx] = True
            days += calculate_days(ny, nx, n, m, visited, maps)
    
    return days
    
def solution(maps):
    answer = []
    c_map = [list(cm) for cm in maps]
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for __ in range(n)]
   
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and c_map[i][j] != 'X':
                visited[i][j] = True
                count = calculate_days(i, j, n, m, visited, c_map)
                
                answer.append(count)
    
    answer.sort()
    
    return answer if len(answer) else [-1]