import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

weights.sort(reverse=True)
boxes.sort(reverse=True)

# 옮길 수 없는 경우
if weights[0] < boxes[0]:
    print(-1); exit()

visited = [False] * m # 상자 방문 여부 저장 리스트
ptr = [0] * n # i번째 크레인이 다음 싸이클 때 보아야하는 상자 번호(index)
answer = 0 # 총 소요 시간 (정답)
moved = 0 # 옮긴 박스 개수
    

while moved < m:
    answer += 1

    for i in range(n):
        while ptr[i] < m:
            if not visited[ptr[i]] and boxes[ptr[i]] <= weights[i]: # 수용 가능한 경우
                visited[ptr[i]] = True 
                moved += 1
                ptr[i] += 1
                break
            ptr[i] += 1 # 수용 불가능한 경우에는 크레인의 포인터 값만 증가
        
print(answer)