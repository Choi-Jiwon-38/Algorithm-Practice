import sys
input = sys.stdin.readline

n = int(input().rstrip())
balloons = list(map(int, input().rstrip().split(" ")))

answer = []
idx = 0

while True:
    answer.append(idx + 1)  # 터뜨린 풍선의 번호를 answer에 추가
    move = balloons[idx]    # 종이에 적힌 수
    balloons[idx] = 0       # 터뜨린 풍선 처리

    if len(answer) == n:
        break

    if move < 0: # 왼쪽 이동
        for i in range(abs(move)):
            idx -= 1
            
            if idx < 0:
                idx += n
            
            while balloons[idx] == 0:
                idx -= 1

                if idx < 0:
                    idx += n
    else: # 오른쪽 이동
        for i in range(move):
            idx += 1

            if idx >= n:
                idx -= n

            while balloons[idx] == 0:
                idx += 1

                if idx >= n:
                    idx -= n
                    

print(*answer)