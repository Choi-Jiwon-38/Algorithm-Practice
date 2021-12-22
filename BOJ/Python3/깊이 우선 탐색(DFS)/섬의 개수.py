# 백준 알고리즘 저지 4963번
# https://www.acmicpc.net/problem/4963

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

def dfs(x, y):
    # 범위를 벗어나는 경우, 바다 지역(0)은 제외
    if x < 0 or x >= h or y < 0 or y >= w or island_map[x][y] == 0:
        return False
    island_map[x][y] = 0 # 현재 위치 방문 처리

    # 상하좌우, 대각선 dfs 실행
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    dfs(x+1, y+1)
    dfs(x+1, y-1)
    dfs(x-1, y+1)
    dfs(x-1, y-1)
    return True


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island_map = [list(map(int, input().split())) for _ in range(h)]
    
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                count += 1
    print(count)
