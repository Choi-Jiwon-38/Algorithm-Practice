# 백준 온라인 저지 2776번

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


T = int(input())

for _ in range(T):
    num1 = int(input())
    suchup1 = list(map(int, input().split()))
    suchup1.sort()

    num2 = int(input())
    suchup2 = list(map(int, input().split()))
    for i in suchup2:
        print(bin_search(suchup1, i))