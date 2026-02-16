import sys
input = sys.stdin.readline

n = int(input())
colors = list(input().rstrip())

curr = colors[0]
b_count = 0
r_count = 0

if curr == 'B':
    b_count = 1
else:
    r_count = 1

for i in range(1, n):
    if curr == colors[i]:
        continue

    curr = colors[i]
    if curr == 'B':
        b_count += 1
    else:
        r_count += 1

print(min(b_count, r_count) + 1) 