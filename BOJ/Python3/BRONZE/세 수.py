# 백준 온라인 저지 10817번

import sys
input = sys.stdin.readline

num_list =  list(map(int, input().split()))
num_list = sorted(num_list)

print(num_list[1])