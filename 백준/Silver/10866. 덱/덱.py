import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
d = deque([])

for _ in range(n):
    cmd = input().rstrip().split(" ")
    
    if cmd[0] == 'push_back':
        d.append(cmd[1])
    elif cmd[0] == 'push_front':
        d.appendleft(cmd[1])
    elif cmd[0] == 'pop_back':
        print(d.pop() if len(d) else -1)
    elif cmd[0] == 'pop_front':
        print(d.popleft() if len(d) else -1)
    elif cmd[0] == 'size':
        print(len(d))
    elif cmd[0] == 'empty':
        print(0 if len(d) else 1)
    elif cmd[0] == 'front':
        print(d[0] if len(d) else -1)
    elif cmd[0] == 'back':
        print(d[-1] if len(d) else -1)