def solution(n, m, section):
    answer = 0
    curr = 0
    
    for i in range(len(section)):        
        if curr >= section[i]:
            i += 1
        else:
            curr = section[i] + m - 1
            answer += 1
    
    
    return answer