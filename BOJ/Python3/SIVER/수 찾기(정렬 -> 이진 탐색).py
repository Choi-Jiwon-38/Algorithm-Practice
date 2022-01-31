# 백준 온라인 저지 1920번
# 정렬 -> 이진 탐색 알고리즘

import sys
from typing import Sequence, Any
input = sys.stdin.readline

def bin_search(a: Sequence, key: Any) -> int:
    a.sort()
    
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif key > a[pc]:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

N = int(input())
temp = list(map(int, input().split()))

M = int(input())
key_list = list(map(int, input().split()))

for k in key_list:
    print(bin_search(temp, k))