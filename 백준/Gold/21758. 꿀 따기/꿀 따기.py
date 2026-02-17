import sys
input = sys.stdin.readline

n = int(input())
places = list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = places[0]

for i in range(1, n):
    prefix_sum[i] = places[i] + prefix_sum[i-1]

answer = 0

# Case 1
# - 벌통이 맨 왼쪽
# - 벌1은 맨 오른쪽
# - 벌2는 벌통과 벌1 사이 어딘가
for i in range(1, n - 1): # i는 벌2의 위치
    bee1 = prefix_sum[n-1] - places[i] - places[n-1]
    bee2 = prefix_sum[i] - places[i] 

    answer = max(answer, bee1 + bee2)

# Case 2
# - 벌통이 중간 어딘가
# - 벌1은 맨 왼쪽
# - 벌2는 맨 오른쪽
for i in range(1, n - 1): # i는 벌통의 위치
    bee1 = prefix_sum[i] - places[0]
    bee2 = prefix_sum[n-1] - prefix_sum[i-1] - places[n-1]

    answer = max(answer, bee1 + bee2)  

# Case 3
# - 벌통이 맨 오른쪽
# - 벌1은 맨 왼쪽
# - 벌2는 벌통과 벌1 사이 어딘가
for i in range(1, n - 1): # i는 벌2의 위치
    bee1 = prefix_sum[n-1] - places[0] - places[i]
    bee2 = prefix_sum[n-1] - prefix_sum[i-1] - places[i]

    answer = max(answer, bee1 + bee2) 

print(answer)