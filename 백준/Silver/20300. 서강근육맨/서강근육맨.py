import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
costs.sort()

answer = 0

if n == 1:
    answer = costs[0]
elif n % 2 == 0:
    i, j = 0, n - 1

    while i < j:
        answer = max(answer, costs[i] + costs[j])
        i += 1
        j -= 1

else:
    i, j = 0, n - 2 

    while i < j:
        answer = max(answer, costs[i] + costs[j])
        i += 1
        j -= 1
    
    answer = max(answer, costs[-1])

print(answer)