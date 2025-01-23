import sys
input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print(0)
elif n <= 3:
    print(1)
else:
    dp = [1e9 for _ in range(n + 1)]
    # base case
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(4, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        dp[i] = min(dp[i], dp[i - 1] + 1)
    
    print(dp[n])