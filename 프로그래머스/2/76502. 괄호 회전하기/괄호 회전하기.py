from collections import deque

dic = {
    "]": "[",
    ")": "(",
    "}": "{",
    "[": None,
    "(": None,
    "{": None,
}


def check(string):
    stack = []
    
    for char in string:
        if len(stack) > 0 and stack[-1] == dic[char]:
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack) == 0


def solution(s):
    answer = 0
    
    for i in range(len(s) - 1):
        s = deque(list(s))
        if check(s):
            answer += 1
        s.rotate(-1)
        
        
    return answer

