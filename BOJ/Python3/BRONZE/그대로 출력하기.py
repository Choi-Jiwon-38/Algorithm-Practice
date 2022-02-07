# 백준 온라인 저지 11718번

import sys
input = sys.stdin.readline
count = 0

while True:
    if count == 100:
        break
    try:
        word = input().rstrip()
        print(word)
        count += 1
    except:
        break