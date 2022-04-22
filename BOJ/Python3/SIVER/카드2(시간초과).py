# 백준 온라인 저지 2164번
import sys
input = sys.stdin.readline

n = int(input())
card = [i for i in range(1, n+1)]

while 1:
    del card[0] # 제일 위에 있는 카드를 버린다
    if len(card) == 1:
        print(card[0])
        break
    if len(card) == 2:
        print(card[0])
        break
    else:
        re = card[0] # 제일 위에 있는 카드를 제일 아랠에 있는 카드
        del card[0]
        card.append(re)