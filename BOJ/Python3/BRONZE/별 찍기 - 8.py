# 백준 온라인 저지 2445번

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    print('*' * i + ' ' * (N-i) * 2 + '*' * i)

for j in range(N-1, 0, -1):
    print('*' * j + ' ' * (N-j) * 2 + '*' * j)