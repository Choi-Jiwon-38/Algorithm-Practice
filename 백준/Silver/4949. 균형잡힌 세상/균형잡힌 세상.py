import sys
input = sys.stdin.readline

while True:
    words = input().rstrip()
    
    if words == '.': break

    stack = []
    
    flag = True

    for char in words:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) < 1 or stack.pop() != '[':
                flag = False
                break
        elif char == ')':
            if len(stack) < 1 or stack.pop() != '(':
                flag = False
                break

    if len(stack) > 0: flag = False
    
    print('yes' if flag else 'no')