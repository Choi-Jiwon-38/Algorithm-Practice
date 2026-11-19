def solution(m, n, puddles):
    maps = [[None for _ in range(m)] for __ in range(n)]
    maps[0][0] = 1
    
    for px, py in puddles:
        maps[py - 1][px - 1] = 0
    
    # y축 초기화
    flag_y = False
    
    for i in range(1, n):
        if flag_y:
            break
            
        if maps[i][0] == 0:
            flag_y = True
        else:
            maps[i][0] = 1
        
    # x축 초기화
    flag_x = False
    
    for i in range(m):
        if flag_x:
            break
        
        if maps[0][i] == 0:
            flag_x = True
        else:
            maps[0][i] = 1 
    
    # 나머지 경로 계산 - dp 이용
    for i in range(1, n):
        for j in range(1, m):
            if maps[i][j] == None:
                left = maps[i][j - 1] if maps[i][j - 1] else 0
                up = maps[i - 1][j] if maps[i - 1][j] else 0
                
                maps[i][j] = (left + up) % 1000000007

    return maps[n - 1][m - 1]