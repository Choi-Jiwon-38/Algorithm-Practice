def solution(want, number, discount):
    wantDic = {}
    
    for i in range(len(want)):
        wantDic[want[i]] = i
    
    currNum = [0 for i in range(len(want))]
    
    for i in range(10):
        if discount[i] in wantDic:
            currNum[wantDic[discount[i]]] += 1
    
    left = 0
    right = 9
    
    answer = 1 if number == currNum else 0
    
    while (right != len(discount) - 1):

        if discount[left] in wantDic:
            currNum[wantDic[discount[left]]] -= 1
        left += 1
        right += 1
        
        if discount[right] in wantDic:
            currNum[wantDic[discount[right]]] += 1
    
        if number == currNum:
            answer += 1

    return answer
