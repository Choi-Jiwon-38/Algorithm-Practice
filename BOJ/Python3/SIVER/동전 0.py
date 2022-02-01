# 백준 온라인 저지 11047번

import sys

N, K = map(int, input().split())

coin_list = []
count = 0

for _ in range(N):
    coin_list.append(int(input()))

coin_list = coin_list[::-1]

for coin in coin_list:
    count += K // coin
    K %= coin

print(count)