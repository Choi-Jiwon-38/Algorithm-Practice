import sys

input = sys.stdin.readline

n, m = map(int, input().split())

temp = []

for i in range(n):
    temp.append(list(map(int, input().split())))

print(temp)