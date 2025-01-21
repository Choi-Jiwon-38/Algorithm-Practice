import sys
input = sys.stdin.readline

n = int(input().rstrip())

triangle_list = []

for i in range(n):
    triangle_list.append(list(map(int, input().rstrip().split(" "))))

for i in range(n - 1, -1, -1):
    if i == 0:
        print(triangle_list[0][0])
        break

    for j in range(i):
        triangle_list[i - 1][j] += max(triangle_list[i][j], triangle_list[i][j + 1])


