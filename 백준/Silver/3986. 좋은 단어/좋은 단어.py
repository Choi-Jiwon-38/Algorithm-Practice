import sys
input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    word = input().rstrip()
    stack = []

    for char in word:
        if len(stack) > 0:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
                
    if len(stack) == 0: answer += 1

print(answer)