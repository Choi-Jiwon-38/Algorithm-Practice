word1 = input()
word2 = input()

n = len(word1)
m = len(word2)

dp = [[0] * m for _ in range(n)] # dp[n][m]

# base case 초기화
for i in range(n):
    if word2[0] == word1[i]:
        dp[i][0] = 1
    else:
        if i > 0:
            dp[i][0] = dp[i - 1][0]

for i in range(m):
    if word1[0] == word2[i]:
        dp[0][i] = 1
    else:
        if i > 0:
            dp[0][i] = dp[0][i - 1]

# recursive case
for i in range(1, n):
    for j in range(1, m):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n - 1][m - 1])