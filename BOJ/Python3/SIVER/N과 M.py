# 백준 온라인 저지 15649번

from ntpath import join
import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

temp = []

for i in range(N): # temp에 1부터 N까지의 자연수를 저장
    temp.append(i+1)

for j in list(permutations(temp, M)):
    word = str(j)
    print((word.replace(',', '')[1:]).replace(')', ''))

