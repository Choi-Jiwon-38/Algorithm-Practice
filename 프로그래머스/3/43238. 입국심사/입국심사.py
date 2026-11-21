def solution(n, times):
    answer = []
    
    s = 1
    e = n * min(times)


    while s <= e:
        m = (s + e) // 2
        
        
        count = sum(m // time for time in times)
        
        if count >= n:
            answer.append(m)
            e = m - 1
        elif count < n:
            s = m + 1
    
    return min(answer)