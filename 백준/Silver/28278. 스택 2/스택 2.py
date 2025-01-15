import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
s = deque()

for _ in range(n):
    cmd = input().rstrip()

    if cmd[0] == '1':
        s.append(int(cmd[2:]))
    elif cmd == '2':
        print(s.pop() if len(s) else -1)
    elif cmd == '3':
        print(len(s))
    elif cmd == '4':
        print(0 if len(s) else 1)
    elif cmd == '5':
        print(s[-1] if len(s) else -1)