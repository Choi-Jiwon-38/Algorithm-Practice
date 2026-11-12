def solution(n, lost, reserve):
    new_lost = []
    
    for l in lost:
        if not l in reserve:
            new_lost.append(l)
        else:
            reserve.remove(l)
            
    new_lost.sort()
    reserve.sort()
    
    l_idx = 0 # lost index
    r_idx = 0 # reserve index
    l_len = len(new_lost) # lost length
    r_len = len(reserve) # reserve length
    
    answer = n - l_len # 학생수 - 체육복 도난당한 학생수
    
    while l_idx < l_len and r_idx < r_len:    
        # 빌려줄 수 없는 경우 (1)
        if reserve[r_idx] < new_lost[l_idx] - 1:
            r_idx += 1
        # 빌려줄 수 없는 경우 (2)
        elif reserve[r_idx] > new_lost[l_idx] + 1:
            l_idx += 1
        else:
            answer += 1
            r_idx += 1
            l_idx += 1
    
    return answer