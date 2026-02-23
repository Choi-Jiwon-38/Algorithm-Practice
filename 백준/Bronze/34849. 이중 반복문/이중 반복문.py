import sys
input = sys.stdin.readline

n = int(input())
print('Time limit exceeded' if n > 10000 else 'Accepted')