import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    
    points = [None, None]
    points[0] = list(map(int, input().rstrip().split(" ")))
    points[1] = list(map(int, input().rstrip().split(" ")))
    
    if n == 1:
        print(max(points[0][0], points[1][0]))
        continue
    
    dp = [[0 for _ in range(n)], [0 for _ in range(n)]]

    # base case
    dp[0][0] = points[0][0]
    dp[1][0] = points[1][0]
    
    dp[0][1] = dp[1][0] + points[0][1]
    dp[1][1] = dp[0][0] + points[1][1]
    
    # recursive case
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + points[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + points[1][i]
        
    print(max(dp[0][n - 1], dp[1][n - 1]))