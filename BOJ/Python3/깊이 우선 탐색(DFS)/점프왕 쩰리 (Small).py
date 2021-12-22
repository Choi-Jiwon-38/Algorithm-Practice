# 백준 알고리즘 저지 16173번
# https://www.acmicpc.net/problem/16173


def dfs(x, y):
    # 게임판 구역을 벗어난 경우, 해당 지점에 이미 방문한 경우
    if 0 > x or x >= n or 0 > y or y >= n or visited[x][y] == True:
        return
    
    # 도착 지점(-1)에 도달한 경우, 방문 처리를 한 뒤 return
    if game_board[x][y] == -1:
        visited[x][y] = True
        return
    
    # 방문 표시 진행
    visited[x][y] = True

    #  쩰리는 오른쪽과 아래로만 이동하므로
    jump = game_board[x][y]
    dfs(x + jump, y)
    dfs(x, y + jump)
    

n = int(input()) # 게임 구역 크기 n 입력

game_board = [] # 게임판 구역(맵) 입력
for i in range(n):
    game_board.append(list(map(int, input().split())))

visited = [[False] * n for i in range(n)]


# 메인 코드
dfs(0, 0)

if visited[n-1][n-1] == True:
    print('HaruHaru')
else:
    print('Hing')

# Debug_space
# print(n)
# print(game_board)
# print(visited)