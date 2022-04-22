# 백준 온라인 저지 10866번
import sys
from collections import deque

deck = deque()
n = int(input())

for _ in range(n):
    cmd = input()
    if cmd == 'size':
        print(len(deck))
    elif cmd == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif cmd == 'back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[len(deck)-1])
    elif cmd == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            n = deck.popleft()
            print(n)
    elif cmd == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            n = deck.pop()
            print(n)
    else:
        cmd, num = cmd.split()
        num = int(num)
        if cmd == 'push_front':
            deck.appendleft(num)
        elif cmd == 'push_back':
            deck.append(num)
        else:
            pass