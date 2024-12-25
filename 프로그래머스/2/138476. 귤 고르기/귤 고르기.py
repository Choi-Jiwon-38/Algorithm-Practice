def solution(k, tangerine):
    dic = {}
    answer = 0
    
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1
    
    values = list(dic.values())
    values.sort(reverse=True)
    
    for v in values:
        answer += 1
        k -= v
        if k <= 0:
            break
        
    return answer