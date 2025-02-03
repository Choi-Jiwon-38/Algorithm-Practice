import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split(" "))
map_arr = [[],[]]
not_visit = [[],[]]

for i in range(2):
    nums = input().rstrip()
    for j in range(n):
        map_arr[i].append(int(nums[j]))
        not_visit[i].append(True)

q = deque([(0, 0, 0)])
answer = 0

not_visit[0][0] = False

while len(q):
    spot, delete_spot, dir = q.popleft()

    if spot + 1 == n or spot + k >= n: # 한 칸 앞 이동이나 점프로 종료되는 경우
        answer = 1
        break
    
    if map_arr[dir][spot + 1] == 1 and not_visit[dir][spot + 1]: # 한 칸 앞 이동이 가능한 경우
        not_visit[dir][spot + 1] = False
        q.append((spot + 1, delete_spot + 1, dir))

    if spot > 0 and spot - 1 > delete_spot and map_arr[dir][spot - 1] == 1 and not_visit[dir][spot - 1]: # 한 칸 뒤로 이동이 가능한 경우
        not_visit[dir][spot - 1] = False
        q.append((spot - 1, delete_spot + 1, dir))

    if map_arr[1 - dir][spot + k] == 1 and not_visit[1 - dir][spot + k] : # 점프가 가능한 경우
        not_visit[1 - dir][spot + k] = False
        q.append((spot + k, delete_spot + 1, 1 - dir)) 

print(answer)