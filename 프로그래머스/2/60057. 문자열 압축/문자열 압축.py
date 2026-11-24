def solution(s):
    answer = len(s)
    n = len(s)
  
    for unit in range(1, n // 2 + 1):
        curr = ''
        count = 0
        new_s = ''
        
        for i in range(0, n + 1, unit):
            if curr != s[i:min(n, i + unit)]:
                if count > 1:
                    new_s += str(count)
                    new_s += curr
                else:
                    new_s += curr
            
                curr = s[i:min(n, i + unit)]
                count = 1
                
                if i + unit > n:
                    new_s += curr
            else:
                count += 1
        
        answer = min(len(new_s), answer)
    
    
    return answer