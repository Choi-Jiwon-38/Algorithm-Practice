import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = []
max_weight = 0
count = 0

for _ in range(n):
    nums.append(int(input().rstrip()))

nums.sort(reverse=True)

for num in nums:
    count += 1
    new_weight = num * count

    if new_weight < max_weight:
        continue

    max_weight = new_weight

print(max_weight)