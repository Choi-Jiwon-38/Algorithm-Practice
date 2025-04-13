alphabet_move_count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def solution(name):
    answer = 0
    n = len(name)
    
    for alphabet in name:
        answer += alphabet_move_count[ord(alphabet) - ord('A')]
        
    move = n - 1 # 0번째 index부터 마지막까지 이동하는 방식 (기본값이자 최대 이동 횟수에 해당)
    
    for i in range(n):
        next_i = i + 1
       
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        # 1. 현재 위치까지 왔다가 뒤로 가기
        move1 = i * 2 + (n - next_i)
        
        # 2. 뒤로 갔다가 현재 위치로 오기
        move2 = 2 * (n - next_i) + i
        
        move = min(move, move1, move2)
            
    
    answer += move
    
    return answer