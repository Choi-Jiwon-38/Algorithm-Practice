# 백준 온라인 저지 1246번

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

buyer_list = []

for _ in range(M):
    buyer_list.append(int(input()))

max_cost = 0
max_benefit = 0
benefit = 0


for cost in range(max(buyer_list)+1):
    benefit = 0
    for buyer in buyer_list:
        if buyer >= cost:
            benefit += cost
            
    if benefit > cost * N:
        benefit = cost * N

    if benefit > max_benefit:
        max_benefit = benefit
        max_cost = cost

print(max_cost, max_benefit)