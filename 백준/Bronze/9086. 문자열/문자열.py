import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input().rstrip()
    answer = w[0] + w[-1]
    print(answer)