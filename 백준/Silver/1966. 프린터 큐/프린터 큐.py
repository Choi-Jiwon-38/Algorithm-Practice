import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print_q =  deque([])
    priority_list = []

    priority_list = list(map(int, input().split()))

    for i in range(len(priority_list)):
        print_q.append((i, priority_list[i]))

    priority_list.sort()

    answer = 0

    while True:
        curr_num, curr_priority = print_q.popleft()

        if curr_priority < priority_list[-1]:
            print_q.append((curr_num, curr_priority))
            continue
        else:
            priority_list.pop()
            answer += 1

            if m == curr_num:
                print(answer)
                break