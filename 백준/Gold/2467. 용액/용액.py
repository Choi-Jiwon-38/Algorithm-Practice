import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

i, j = 0, n-1

answer = []
min_diff = float('inf')

while i < j:
    curr_sum = liquids[i] + liquids[j]
    diff_from_zero = abs(curr_sum)
    
    if diff_from_zero < min_diff:
        min_diff = diff_from_zero
        answer = [liquids[i], liquids[j]]
    
    if curr_sum > 0:
        j -= 1
    else:
        i += 1

print(*answer)