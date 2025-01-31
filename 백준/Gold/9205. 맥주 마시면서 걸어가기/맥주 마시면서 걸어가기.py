import sys
from collections import deque
input = sys.stdin.readline
MAX_DIST = 1000

t = int(input().rstrip())

def get_dist(curr, target):
    return abs(target[1] - curr[1]) + abs(target[0] - curr[0])

def bfs(q, end, stores, alive):
    visits = set()
    while len(q):
        curr = q.popleft()
        visits.add(curr)

        if get_dist(curr, end) <= MAX_DIST:
            alive[0] = True
            break

        for store in stores:
            if not store in visits and get_dist(curr, store) <= MAX_DIST: 
                q.append(store)

for _ in range(t):
    alive = [False]
    
    n = int(input().rstrip())

    q = deque([tuple(map(int, input().rstrip().split(" ")))])
    stores = [tuple(map(int, input().rstrip().split(" "))) for _ in range(n)]
    end = tuple(map(int, input().rstrip().split(" ")))

    bfs(q, end, stores, alive)
    print('happy' if alive[0] else 'sad')