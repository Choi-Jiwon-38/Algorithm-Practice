# 백준 온라인 저지 11170번

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    count = 0
    for i in range(N, M+1):
        word = str(i)
        for j in word:
            if j == '0':
                count += 1
    print(count)