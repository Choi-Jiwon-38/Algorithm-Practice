import sys
input = sys.stdin.readline

n = int(input().rstrip())
data_list = []
swap_list = []

for index in range(n):
    data_list.append([int(input().rstrip()), index])

data_list.sort()

for index in range(n):
    swap_list.append(data_list[index][1] - index)

print(max(swap_list) + 1)