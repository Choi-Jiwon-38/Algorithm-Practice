# 백준 온라인 저지 23037번

import sys
input = sys.stdin.readline

num = input().rstrip()
answer = 0

for n in num:
    answer += int(n)**5

print(answer)