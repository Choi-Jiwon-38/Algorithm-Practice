# 백준 온라인 저지 15650번

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

temp = []
for i in range(N):
    temp.append(i+1)

for j in list(combinations(temp, M)):
    word = str(j)
    print((word.replace(',', '')[1:]).replace(')', ''))