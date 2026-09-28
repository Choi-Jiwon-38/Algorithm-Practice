from collections import deque

match = {
    ']': '[',
    ')': '(',
    '}': '{',
    '[': None,
    '(': None,
    '{': None
}


def check(s):
    stack = []
    
    for c in s:
        if len(stack) and stack[-1] == match[c]:
            stack.pop()
        else:
            stack.append(c)
    
    return False if len(stack) else True
    
    

def solution(s):
    s = deque(s)
    answer = 0
    
    if check(s):
        answer += 1
    
    
    for i in range(len(s) - 1):
        s.rotate(-1)
        if check(s):
            answer += 1
    
    
    
    return answer