import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    stack = []
    ps = list(input().rstrip())
    
    for p in ps:
        if len(stack):
            if p == '(':
                stack.append(p)
            else:                       # p == ')'
                if stack[-1] == '(':    # 괄호 짝이 맞으므로 지움
                    stack.pop()
                else:                   # stack[-1] == ')'
                    stack.append(p)
        else:                           # 스택이 비어있는 경우
            stack.append(p)

    print('NO' if len(stack) else 'YES')