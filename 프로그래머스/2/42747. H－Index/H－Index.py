def solution(citations):
    answer = 0
    
    n = len(citations)
    citations.sort()
    
    for h in range(n + 1):
        i = 0
        while i < n and citations[i] < h:
            i += 1
        
        # h번 이상 인용된 논문 수
        count = n - i
        
        if count >= h:
            answer = h
        
    return answer