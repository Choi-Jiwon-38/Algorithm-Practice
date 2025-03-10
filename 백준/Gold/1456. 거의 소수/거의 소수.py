import sys
import math
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(" "))

nums = [True] * (10000001)

nums[0] = False
nums[1] = False

for i in range(2, math.ceil((10000001) ** 0.5)):
    if not nums[i]:
        continue

    for j in range(2 * i, 10000001, i):
        nums[j] = False

answer = 0

for i in range(2, 10000001):
    if nums[i]:
        temp = i

        while i <= (b / temp):
            if i >= (a / temp):
                answer += 1
            temp = temp * i

print(answer)