import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    print(f'{(h if n % h == 0 else n % h)}{(n // h if n % h == 0 else n // h + 1):02}')
    2