import sys
from collections import deque
input = sys.stdin.readline
MAX_RANGE = 100001

n, k = map(int, input().rstrip().split(" "))

if n == k:
    print(0)
else:
    visited = [False] * MAX_RANGE
    min_time = float('inf')
    
    q = deque([(0, n)]) # 시간, 노드
    visited[n] = True

    while len(q):
        time, node = q.popleft()

        if time >= min_time:
            continue

        if node == k:
            min_time = time
            break

        if 2 * node < MAX_RANGE and not visited[node * 2]:
            visited[node * 2] = True
            q.append((time, node * 2))
        
        if node - 1 >= 0 and not visited[node - 1]:
            visited[node - 1] = True
            q.append((time + 1, node - 1))

        if node + 1 < MAX_RANGE and not visited[node + 1]:
            visited[node + 1] = True
            q.append((time + 1, node + 1))
        
    print(min_time)