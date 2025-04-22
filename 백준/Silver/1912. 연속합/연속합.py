import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split(" ")))
dp = [0] * n

# base case
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], arr[i] + dp[i-1])

print(max(dp))