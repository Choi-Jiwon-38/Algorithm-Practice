#  백준 온라인 저지 10845번

import sys

input = sys.stdin.readline

def command(cmd):
    if cmd[0:4] == "push":
        que.append(int(cmd[5:]))
    elif cmd == "pop":
        if len(que) == 0:
            print(-1)
        else:
            pop_num = que[0]
            que.remove(pop_num)
            print(pop_num)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else: # cmd == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que)-1])

que = []

n = int(input())
for _ in range(n):
    command(input().rstrip())