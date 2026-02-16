import sys
input = sys.stdin.readline

c, n = map(int, input().split())

city_infos = []

for _ in range(n):
    cost, reward = map(int, input().split())
    city_infos.append((cost, reward))

dp = [float('inf')] * (c + 101)

# base case
dp[0] = 0

for info in city_infos:
    cost, reward = info
    for i in range(reward, len(dp)):
        dp[i] = min(dp[i], dp[i - reward] + cost) 

print(min(dp[c:c+100]))