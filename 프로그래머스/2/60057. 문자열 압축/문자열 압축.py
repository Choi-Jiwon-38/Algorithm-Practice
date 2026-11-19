def solution(s):
    answer = len(s)
    
    for unit in range(1, len(s) // 2 + 1):
        new_s = ''
        curr_base = ''
        count = 0
        
        for i in range(0, len(s) + 1, unit):         
            if curr_base == s[i:min(i + unit, len(s))]:
                count += 1
            else:
                if count <= 1:
                    new_s += curr_base
                else:
                    new_s += str(count)
                    new_s += curr_base
                
                
                curr_base = s[i:min(i + unit, len(s))]
                count = 1
                
                # 이 부분이 누락되는 건 보이는데, 위 조건식을 조정해서 해결할 방법은 없는지..?
                if i + unit > len(s):
                    new_s += curr_base
                
        
        answer = min(answer, len(new_s))
    
    return answer