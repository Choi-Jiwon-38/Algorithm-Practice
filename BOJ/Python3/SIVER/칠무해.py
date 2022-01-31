# 백준 온라인 저지 14729번

import sys
input = sys.stdin.readline

scoreList = []

N = int(input())

for _ in range(N):
    scoreList.append(float(input()))

scoreList.sort()

for i in range(7):
    print(f'{scoreList[i]:.3f}')