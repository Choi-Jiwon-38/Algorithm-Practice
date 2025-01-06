from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for i in range(len(priorities)):
        q.append([priorities[i], i])
        
    priority_list = sorted(list(q))
    it = len(priority_list) - 1
    
    while True:
        if q[0][0] < priority_list[it][0]:
            tmp = q.popleft()
            q.append(tmp)
        else:
            answer += 1
            tmp = q.popleft()
            if tmp[0] == priority_list[it][0]:
                it -= 1
            
            if tmp[1] == location:
                return answer
    
