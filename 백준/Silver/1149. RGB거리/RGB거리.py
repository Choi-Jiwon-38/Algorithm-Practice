import sys
input = sys.stdin.readline

n = int(input().rstrip())

costs = []
dp = []

for _ in range(n):
    costs.append(list(map(int, input().rstrip().split(" "))))
    dp.append([0, 0, 0])

dp[0] = costs[0]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

print(min(dp[n-1]))