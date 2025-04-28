import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split(" "))

coins = set()

for i in range(n):
    coin = int(input().rstrip())
    if coin <= k:
        coins.add(coin)

coin_list = sorted(list(coins))

dp = [float('inf')] * (k + 1)

for coin in coin_list:
    dp[coin] = 1

for i in range(1, k + 1):
    for coin in coin_list:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])

