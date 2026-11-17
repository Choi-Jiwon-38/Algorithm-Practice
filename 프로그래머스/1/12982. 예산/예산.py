def solution(d, budget):
    d.sort()
    i = 0
    answer = 0
    
    while i < len(d) and d[i] <= budget:
        answer += 1
        budget -= d[i]
        i += 1
    
    return answer