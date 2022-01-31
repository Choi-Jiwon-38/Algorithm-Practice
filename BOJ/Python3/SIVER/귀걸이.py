# 백준 온라인 저지 1380번

import sys
input = sys.stdin.readline

scenario = 1

while 1:
    n = int(input())
    if n == 0:
        break
    std = []
    cnt = [0] * n
    
    for _ in range(n):
        std.append(input().rstrip())

    for _ in range(2*n-1):
        num, alp = input().split()
        cnt[int(num)-1] += 1

    for i in range(n):
        if cnt[i] == 1:
            print(scenario, std[i])
            break

    scenario += 1