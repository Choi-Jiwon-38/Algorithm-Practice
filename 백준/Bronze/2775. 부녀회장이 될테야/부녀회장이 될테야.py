import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    n = int(input().rstrip())

    arr = [[0] * (n + 1)] * (k + 1)

    for i in range(1, n + 1):
        arr[0][i] = i
    
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j]
    
    print(arr[k][n])