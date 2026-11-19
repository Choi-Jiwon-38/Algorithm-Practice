

def solution(number, k):
    answer = ''
    rest = k
    stack = []

    for num in list(number):
        if rest == 0:
            stack.append(num)
            continue
        
        if stack and stack[-1] < num:
            while rest and stack and stack[-1] < num:
                stack.pop()
                rest -= 1
                
            stack.append(num)
        else:
            stack.append(num)
    
    
    if rest:
        stack = stack[:-rest]

    return ''.join(stack)