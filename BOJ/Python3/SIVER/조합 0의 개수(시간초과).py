# 백준 온라인 저지 2004번

import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())

nCm = str(int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m))))

nCm = nCm[::-1]
count = 0

for i in nCm:
    if i == '0':
        count += 1
    else:
        break

print(count)