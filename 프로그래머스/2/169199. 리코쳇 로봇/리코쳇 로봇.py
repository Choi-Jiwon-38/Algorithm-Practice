from collections import deque

def solution(board):
    max_y = len(board)
    max_x = len(board[0])
    start_y = None
    start_x = None
    goal_y = None
    goal_x = None
    answer = -1
    
    
    
    visited = [[[False, False, False, False] for _ in range(max_x)] for _ in range(max_y)]
    
    for i in range(max_y):
        for j in range(max_x):
            if board[i][j] == 'G':
                goal_y = i
                goal_x = j
            
            if board[i][j] == 'R':
                start_y = i
                start_x = j
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dq = deque([])
    
    def can_move(y, x, d, visited):
        if 0 <= y and y < max_y and 0 <= x and x < max_x and visited[y][x][d] == False:
            return True
        else:
            return False
    
    for i in range(4):        
        if can_move(start_y, start_x, i, visited):
            visited[start_y][start_x][i] = True
            dq.append((start_y, start_x, i, 0))
            
    while dq:
        cy, cx, cd, dist = dq.popleft()
        dy, dx = dirs[cd]
        
        if cy == goal_y and cx == goal_x:
            return dist
        
        ny, nx = cy, cx
        
        while 0 <= ny + dy and ny + dy < max_y and 0 <= nx + dx and nx + dx < max_x and board[ny + dy][nx + dx] != 'D':
            ny += dy
            nx += dx
        
        for i in range(4):        
            if can_move(ny, nx, i, visited):
                visited[ny][nx][i] = True
                dq.append((ny, nx, i, dist + 1)) 
    
    
    return answer