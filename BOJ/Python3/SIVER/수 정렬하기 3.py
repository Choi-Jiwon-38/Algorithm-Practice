# 백준 온라인 저지 10989번

import sys
input = sys.stdin.readline

max_num = 10000 # 입력될 수 있는 수의 최댓값
n = int(input()) # 입력받는 숫자의 개수

count = [0] * (max_num + 1) # 각 숫자가 입력된 개수를 저장할 배열 / 0으로 초기화

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(max_num + 1):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)