import sys
from unittest import result
input = sys.stdin.readline

N = int(input()) # 입력받을 좌표의 개수 N

dot_list = [] # N개의 좌표를 입력받을 빈 리스트 생성

for _ in range(N):
    dot_list.append(list(map(int, input().split())))

dot_list.append(dot_list[0]) # 신발끈 공식을 사용하기 위해 첫 번째 좌표를 마지막에 추가

result = 0

for i in range(N):
    result += dot_list[i][0] * dot_list[i+1][1] - dot_list[i][1] * dot_list[i+1][0] # 신발끈 공식 이용


print(abs(result/2))