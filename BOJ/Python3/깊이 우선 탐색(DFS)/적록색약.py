# 백준 알고리즘 저지 10026번
# https://www.acmicpc.net/problem/10026


import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

picture_1 = [] # 
picture_2 = [] #

for _ in range(N):
    piece = input().strip()
    picture_1.append(list(piece))
    picture_2.append(list(piece.replace('R', 'G')))

# print(picture_1)
# print(picture_2)

def dfs(x, y, visited, picture):
    # 구역을 벗어나거나 이미 방문한 경우 제외
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y] == True:
        return False
    # 현재 구역 방문 처리
    visited[x][y] = True

    try:
        if picture[x][y] == picture[x+1][y]:
            dfs(x+1, y, visited, picture)
    except:
        pass

    try:
        if picture[x][y] == picture[x-1][y]:
            dfs(x-1, y, visited, picture)
    except:
        pass

    try:
        if picture[x][y] == picture[x][y+1]:
            dfs(x, y+1, visited, picture)
    except:
        pass

    try:
        if picture[x][y] == picture[x][y-1]:
            dfs(x, y-1, visited, picture)
    except:
        pass


    return True

visited_1 = [[False] * N for _ in range(N)]
visited_2 = [[False] * N for _ in range(N)]

count_1 = 0
count_2 = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j, visited_1, picture_1):
            count_1 += 1
        if dfs(i, j, visited_2, picture_2):
            count_2 += 1

print(str(count_1) + " " + str(count_2))