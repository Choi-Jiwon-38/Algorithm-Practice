def solution(board, h, w):
    n = len(board)
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    answer = 0
    
    for dy, dx in dirs:
        ny = h + dy
        nx = w + dx
        
        if ny >= 0 and ny < n and nx >= 0 and nx < n and board[h][w] == board[ny][nx]:
            answer += 1
    
    return answer