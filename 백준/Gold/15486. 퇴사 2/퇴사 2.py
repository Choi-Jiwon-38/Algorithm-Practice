import sys
input = sys.stdin.readline

n = int(input())
schedules = [0] * n
dp = [0] * (n + 1) # 마지막 날 1일 상담과 같은 케이스 고려 필요

for i in range(n):
    t, p = map(int, input().split())
    schedules[i] = (t, p)

    if i > 0:
        if dp[i-1] > dp[i]: dp[i] = dp[i-1]

    if i + t > n:
        continue
    else:
        j = i + t
            
        if dp[i] + p > dp[j]:
            dp[j] = dp[i] + p

if dp[n-1] > dp[n]: dp[n] = dp[n-1]

print(dp[n])