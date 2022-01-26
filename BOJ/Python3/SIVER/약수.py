# 백준 온라인 저지 1037번
# 

import sys
input = sys.stdin.readline

N = int(input())
yaksu = list(map(int, input().split()))

yaksu = sorted(yaksu)

print(yaksu[0] * yaksu[N-1])