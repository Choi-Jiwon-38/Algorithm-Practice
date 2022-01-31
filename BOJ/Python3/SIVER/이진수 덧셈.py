# 백준 온라인 저지 2729번

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n1, n2 = input().split()
    print(bin(int(n1, 2) + int(n2, 2))[2:])