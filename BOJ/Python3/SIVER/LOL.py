# 백준 온라인 저지 11140번

import sys
input = sys.stdin.readline

def LOL(word):
    if 'lol' in word:
        print(0)
    elif 'll' in word:
        print(1)
    elif 'lo' in word:
        print(1)
    elif 'ol' in word:
        print(1)
    elif 'l' in word:
        print(2)
    elif 'o' in word:
        print(2)
    else:
        print(3)

n = int(input())

for i in range(n):
    LOL(input().rstrip())
