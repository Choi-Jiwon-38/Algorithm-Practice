from collections import deque

def solution(s):
    q = deque()
    
    for c in s:
        if len(q) == 0:
            q.append(c)
        else:
            if q[-1] == c:
                q.pop()
            else:
                q.append(c)
            
    return 1 if len(q) == 0 else 0