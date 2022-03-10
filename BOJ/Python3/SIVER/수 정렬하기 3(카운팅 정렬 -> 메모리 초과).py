# 백준 온라인 저지 10989번
# HINT: counting sort(계수 정렬)를 이용하여 푼다.
# counting sort를 구현하며 참고한 사이트 -> https://bowbowbow.tistory.com/8

import sys
input = sys.stdin.readline

max_num = 10000 # 입력될 수 있는 수의 최댓값
n = int(input()) # 입력받는 숫자의 개수

count = [0] * (max_num + 1) # 각 숫자가 입력된 개수를 저장할 배열 / 0으로 초기화
count_sum = [0] * (max_num + 1) # 위 count의 누적합을 저장할 배열 / 0으로 초기화

input_num = []

for _ in range(n):
    num = int(input())
    input_num.append(num)
    count[num] += 1

# 각 숫자의 입력 개수를 토대로 누적합 값을 갱신
count_sum[0] = count[0]

for i in range(1, max_num + 1):
    count_sum[i] = count_sum[i-1] + count[i]


answer = [0] * (n + 1)

for j in range(n-1, -1, -1): # j에는 n-1부터 0까지 순차적으로 1씩 수가 감소하면서 들어감 (역순으로 돌아가며 수 점검)
    answer[count_sum[input_num[j]]] = input_num[j]
    count_sum[input_num[j]] -= 1


for k in range(1, len(answer)):
    print(answer[k])