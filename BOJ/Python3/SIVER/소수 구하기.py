# 백준 온라인 저지 1929번
# https://www.acmicpc.net/problem/1929

import sys

input = sys.stdin.readline

M, N = map(int, input().split()) #

prime = [None] * 500000

prime[0], prime[1] = 2, 3
ptr = 2

for n in range(5, N, 2): # M까지 수들 중에서 홀수만 탐색
    i = 1
    while prime[i] ** 2 <= n:
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1

if N == 2:
    print(2)
else:
    for i in range(ptr):
        if prime[i] >= M:
            print(prime[i])