import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))
nums = sorted(list(map(int, input().rstrip().split(" "))))

answer = []

def backtrack(depth = 0):
    if depth == m:
        print(*answer)
        return True
    
    visit_in_depth = []
    
    for num in nums:
        if not num in visit_in_depth and (not len(answer) or num >= answer[-1]):
            visit_in_depth.append(num)
            answer.append(num)
            backtrack(depth + 1)
            answer.pop()

backtrack()