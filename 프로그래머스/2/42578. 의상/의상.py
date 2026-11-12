def solution(clothes):
    answer = 1
    cloth_dict = dict()
    
    # n - name / t - type
    for n, t in clothes:
        if t in cloth_dict:
            cloth_dict[t].append(n)
        else:
            cloth_dict[t] = [n] 
    
    for val in cloth_dict.values():
        answer *= (len(val) + 1)
    
    # 아무것도 안 입는 경우 제외
    answer -= 1
    
    return answer