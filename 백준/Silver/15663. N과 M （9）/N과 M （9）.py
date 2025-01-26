import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))
nums = sorted(list(map(int, input().rstrip().split(" "))))

answer = []
used_index = []

def backtrack(depth = 0):
    if depth == m:
        print(*answer)
        return True
    
    visit_in_depth = []

    for i in range(n):
        num = nums[i]
        if not num in visit_in_depth and not i in used_index:
            visit_in_depth.append(num)
            used_index.append(i)
            answer.append(num)
            backtrack(depth + 1)
            used_index.pop()
            answer.pop()

backtrack()