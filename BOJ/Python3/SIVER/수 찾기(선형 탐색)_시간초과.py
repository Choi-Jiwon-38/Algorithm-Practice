# 백준 온라인 저지 1920번

# 선형 탐색 알고리즘(보초법으로 개선)
import sys
import copy
from typing import Sequence, Any
input = sys.stdin.readline

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)
    
    i = 0
    while 1:
        if a[i] == key:
            break
        i += 1
    return 0 if i == len(seq) else 1

N = int(input())
temp = list(map(int, input().split()))

M = int(input())
key_list = list(map(int, input().split()))

for k in key_list:
    print(seq_search(temp, k))