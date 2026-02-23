import sys
input = sys.stdin.readline
s, m = map(int, input().split())

if (s > 1000 or m > 1000) or (s + m) % 2 != 0 or m > s:
    print(-1)
    exit()

a = (s + m) // 2
b = s - a

print(a, b)