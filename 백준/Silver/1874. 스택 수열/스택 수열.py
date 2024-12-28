import sys
input = sys.stdin.readline

n = int(input().rstrip())

answer = []
stack = []

enable = True
num = 1 # 자연수

for _ in range(n):
    su = int(input().rstrip())
    if (num <= su):
        while num <= su:
            stack.append(num)
            answer.append('+')
            num += 1
        stack.pop()
        answer.append('-')
    
    else: # su < num:
        answer.append('-')
        if (su > stack.pop()):
            enable = False
            break

if (enable):
    for i in answer:
        print(i)
else:
    print('NO')