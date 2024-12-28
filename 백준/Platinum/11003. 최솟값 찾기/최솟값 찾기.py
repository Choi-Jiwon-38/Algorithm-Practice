import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().rstrip().split(" "))
a = list(map(int, input().rstrip().split(" ")))

dq = deque()

for i in range(n):
    index, value = i, a[i]
    
    while len(dq) != 0 and dq[-1][1] > value:
        dq.pop()
    
    dq.append([index, value])
    
    if (dq[0][0] <= index - l):
        dq.popleft()
    
    print(dq[0][1], end=' ')