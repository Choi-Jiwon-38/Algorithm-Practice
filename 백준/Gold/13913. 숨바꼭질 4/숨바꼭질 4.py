import sys
from collections import deque
input = sys.stdin.readline
MAX_RANGE = 100001

n, k = map(int, input().rstrip().split(" "))
visited = [-1] * MAX_RANGE

if n == k:
    print(0)
    print(n)
else:
    q = deque([(n, 0)]) # 노드, 시간
    visited[n] = n

    while len(q):
        node, prev_time = q.popleft()
        curr_time = prev_time + 1

        if 2 * node < MAX_RANGE and not visited[2 * node] != -1:
            visited[2 * node] = node
            if 2 * node == k:
                print(curr_time)
                break
            else:
                q.append((2 * node, curr_time))
        
        if node + 1 < MAX_RANGE and not visited[node + 1] != -1:
            visited[node + 1] = node
            if node + 1 == k:
                print(curr_time)
                break
            else:
                q.append((node + 1, curr_time))
        
        if node - 1 >= 0 and not visited[node - 1] != -1:
            visited[node - 1] = node
            if node - 1 == k:
                print(curr_time)
                break
            else:
                q.append((node - 1, curr_time))

    answer = ''
    idx = k

    while True:
        answer = str(idx) + ' ' + answer
        if visited[idx] == idx:
            break
        idx = visited[idx]

    print(answer.rstrip())