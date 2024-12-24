def solution(clothes):
    dic = {}
    answer = 1
    
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        if not key in dic:
            dic[key] = []
        
        dic[key].append(value)
        
    values = list(dic.values())
    
    for value in values:
        answer *= (len(value) + 1)
    
    # 아무것도 선택하지 않는 경우
    answer -= 1

    return answer