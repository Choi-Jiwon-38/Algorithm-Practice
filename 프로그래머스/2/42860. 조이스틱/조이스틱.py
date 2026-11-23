def solution(name):
    answer = 0
    n = len(name)        
    dists = []
        
    for i in range(n):
        answer += min(ord('Z') - ord(name[i]) + 1, ord(name[i]) - ord('A'))
        if name[i] != 'A':
            dists.append(i)
    
    move = n - 1
    
    for i in range(n):
        next_i = i + 1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        
        # 1. 현 위치까찌 왔다가 뒤로가기
        move1 = i * 2 + (n - next_i)
        
        # 2. 뒤로 갔다가 현재 위치로 오기
        move2 = 2 * (n - next_i) + i
        
        move = min(move, move1, move2)
    
    answer += move
    
    return answer