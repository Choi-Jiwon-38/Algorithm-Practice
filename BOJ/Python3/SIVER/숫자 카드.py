# 백준 온라인 저지 10815번

import sys
input = sys.stdin.readline

def bin_search(a, key):
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl + pr) // 2
        
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

N = int(input())
card1 = list(map(int, input().split()))
card1.sort()

M = int(input())
card2 = list(map(int, input().split()))

word = ''

for c in card2:
    word += str(bin_search(card1, c))
    word += ' '

print(word.rstrip())