# 백준 알고리즘 저지 1012번
# https://www.acmicpc.net/problem/1012


import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(x, y): # dfs 함수 생성
    if x <= -1 or x >= N or y <= -1 or y >= M or field[x][y] == 1:
        return False
    
    # 현재 노드 방문 처리
    field[x][y] = 1
    # 상하좌우 재귀적으로 호출
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True


T = int(input()) # 테스트 케이스의 개수 입력

for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 위치 입력

    field = [[1]*M for i in range(N)] # 1로 초기화된 배추 텃밭 생성
    for _ in range(K): # 배추가 있는 곳은 0으로 초기회
        y, x = map(int, input().split())
        field[x][y] = 0

    result = 0
    for i in range(N):
        for j in range(M):
            # 현재 위치에서 dfs 실행
            if dfs(i, j) == True:
                result += 1

    print(result)