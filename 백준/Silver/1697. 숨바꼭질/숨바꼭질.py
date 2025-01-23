import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split(" "))

q = deque([])
visit = [False for _ in range(100001)]

def valid(num):
    if num < 0 or num > 100000 or visit[num]:
        return False
    return True

def bfs(): # 깊이가 곧 time과 같음
    while len(q):
        loc, time = q.popleft()

        if loc == k:
            print(time)
            break
        
        if valid(loc - 1):
            visit[loc - 1] = True
            q.append([loc - 1, time + 1])
        
        if valid(loc + 1):
            visit[loc + 1] = True
            q.append([loc + 1, time + 1])

        if valid(loc * 2):
            visit[loc * 2] = True
            q.append([loc * 2, time + 1])

q.append([n, 0])
visit[n] = True
bfs()