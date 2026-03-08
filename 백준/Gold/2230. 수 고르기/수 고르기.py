import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
i, j = 0, 0

answer = float('inf')


while i < n and j < n:
    diff = abs(a[j] - a[i])
    
    if diff >= m:
        answer = min(answer, diff)

    if diff < m:
        j += 1
    elif diff == m:
        break
    else:
        i += 1         

print(answer)