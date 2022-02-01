# 백준 온라인 저지 1676번

import math, sys

input = sys.stdin.readline

num = str(math.factorial(int(input())))
num = num[::-1]

count = 0

for i in num:
    if i == '0':
        count += 1
    else:
        break

print(count)