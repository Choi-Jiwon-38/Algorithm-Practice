import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

q = deque([])

for _ in range(n):
    cmd = input().rstrip()

    if cmd.startswith('push'):
        _, num = cmd.split(" ")
        q.append(int(num))
    elif cmd == 'front':
        print(q[0] if q else -1)
    elif cmd == 'back':
        print(q[-1] if q else -1)
    elif cmd == 'empty':
        print(0 if q else 1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'pop':
        print(q.popleft() if q else -1)