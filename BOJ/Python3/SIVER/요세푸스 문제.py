# 백준 온라인 저지 1158번
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

answerList = deque()
numList = deque()

for i in range(1, N+1):
    numList.append(i)

if N != 1:
    while len(numList) != 2:
        num = numList[K-1]
        answerList.append(num)
        numList.remove(num)
        numList.rotate(-(K-1))

    if K%2 == 1:
        answerList.append(numList[0])
        answerList.append(numList[1])
    else:
        answerList.append(numList[1])
        answerList.append(numList[0])

    answerWord = ''
    for j in range(N):
        answerWord += str(answerList[j])
        if j == N - 1:
            break
        answerWord += ', '
else:
    answerWord = str(N)

print('<' + answerWord + '>')


# 5000 5000 입력하면 인덱스 오류 남 <- 해결해줘 응애