# 백준 온라인 저지 5585번

import sys

input = sys.stdin.readline

coin_list = [500, 100, 50, 10, 5, 1]
count = 0

item = 1000 - int(input())

for coin in coin_list:
    count += item // coin
    item %= coin

print(count)