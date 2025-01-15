import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = [num for num in range(1, n + 1)]
result = []

def backtrack(depth = 0):
    if depth == m:
        print(*result)
        return
    
    for num in nums:
        if depth == 0 or result[-1] <= num:
            result.append(num)
            backtrack(depth + 1)
            result.pop()

backtrack()