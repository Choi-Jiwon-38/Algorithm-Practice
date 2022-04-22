# 백준 온라인 저지
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
card = deque()

for i in range(1, n+1):
    card.append(i)

while 1:
    if len(card) == 1:
        print(card[0])
        break
    a = card.pop() 
    if len(card) == 1:
        print(card[0])
        break
    card.rotate(-1)