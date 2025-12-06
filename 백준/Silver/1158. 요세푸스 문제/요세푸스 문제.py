import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))

arr = [i for i in range(1, n + 1)]
answer = []
idx = 0

while n > 0:
    idx = (idx + k - 1) % n
    answer.append(str(arr[idx]))
    arr.pop(idx)
    n -= 1

print('<' + ', '.join(answer) + '>')