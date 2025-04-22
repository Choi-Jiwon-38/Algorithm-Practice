import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * (n - 10)

    for i in range(11, n + 1):
        arr[i] = arr[i - 1] + arr[i - 5]
    
    print(arr[n])