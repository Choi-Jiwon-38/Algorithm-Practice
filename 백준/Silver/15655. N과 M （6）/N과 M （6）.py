import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split(" "))
nums = sorted(list(map(int, input().rstrip().split(" "))))
answer = []

def backtrack(depth = 0):
    if depth == m:
        print(*answer)
        return

    for num in nums:
        if not num in answer and (not len(answer) or answer[-1] < num) :
            answer.append(num)
            backtrack(depth + 1)
            answer.pop()

backtrack()