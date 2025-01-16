import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

temp = []

for i in range(N):
    temp.append(i+1)

for j in list(permutations(temp, M)):
    word = str(j)
    print((word.replace(',', '')[1:]).replace(')', ''))