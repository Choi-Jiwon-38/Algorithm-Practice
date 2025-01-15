import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(" "))

def dfs(a, b, num = 1):
    if a == b:
        return num

    if a > b:
        return float('inf')
    
    case1 = dfs(a * 2, b, num + 1)
    case2 = dfs(int(str(a) + '1'), b, num + 1)

    return min(case1, case2)
    
answer = dfs(a, b)

print(answer if answer != float('inf') else -1)