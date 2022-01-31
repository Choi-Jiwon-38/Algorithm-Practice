# 백준 온라인 저지 1769번

import sys
input = sys.stdin.readline

num = input().rstrip()
cnt = 0

while True:
    new_num = 0
    for i in range(len(num)):
        new_num += int(num[i])
    cnt += 1
    num = str(new_num)
    if len(num) == 1:
        break

print(cnt)
if int(num) % 3 == 0:
    print('YES')
else:
    print('NO')
