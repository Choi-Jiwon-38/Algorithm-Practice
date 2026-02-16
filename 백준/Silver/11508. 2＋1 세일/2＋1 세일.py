import sys
input = sys.stdin.readline

n = int(input())
prices = []

for _ in range(n):
    prices.append(int(input()))

prices.sort()

answer = 0

while len(prices) >= 3:
    f, s, free = prices.pop(), prices.pop(), prices.pop() 
    answer += f + s

while len(prices):
    answer += prices.pop()

print(answer)