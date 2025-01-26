import sys
input = sys.stdin.readline

N = int(input().rstrip())

table = list(map(int, input().rstrip().split(" ")))
prev_max = prev_min = table

for i in range(1, N):
    table = list(map(int, input().rstrip().split(" ")))
    
    curr_max = [-float('inf') for _ in range(3)]
    curr_min = [float('inf') for _ in range(3)]

    for j in range(3):
        if j > 0:
            curr_max[j - 1] = max(curr_max[j - 1], table[j - 1] + prev_max[j])
            curr_min[j - 1] = min(curr_min[j - 1], table[j - 1] + prev_min[j])
        
        curr_max[j] = max(curr_max[j], table[j] + prev_max[j])
        curr_min[j] = min(curr_min[j], table[j] + prev_min[j])
        
        if j < 2:
            curr_max[j + 1] = max(curr_max[j + 1], table[j + 1] + prev_max[j])
            curr_min[j + 1] = min(curr_min[j + 1], table[j + 1] + prev_min[j])

    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))