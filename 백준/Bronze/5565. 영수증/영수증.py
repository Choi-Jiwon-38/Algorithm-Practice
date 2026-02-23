import sys
input = sys.stdin.readline
answer = int(input())
for _ in range(9): answer -= int(input())
print(answer)