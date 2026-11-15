def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n):
        flag = False
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                flag = True
                answer.append(j - i)
                break
        
        if not flag:
            answer.append(n - i - 1)
        
    return answer