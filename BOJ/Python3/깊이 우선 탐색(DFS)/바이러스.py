# 백준 온라인 저지 2606번
# https://www.acmicpc.net/problem/2606

virus = {}
virus_list = []

computer = int(input()) # 컴퓨터의 수 입력
n = int(input()) # 연결된 네트워크 수

for _ in range(computer): # 연결된 컴퓨터를 표현하기 위한 빈 리스트
    virus_list.append([])

for i in range(n): # 연결된 컴퓨터를 virus_list에 추가
    f, s = map(int, input().split())
    virus_list[f-1].append(s)
    virus_list[s-1].append(f)

for j in range(computer): # dfs를 위한 딕셔너리 생성
    virus[j+1] = virus_list[j]

visited = [False] * (computer + 1) # 방문노드 작성

# dfs 구현
def dfs(virus, v, visited):
    visited[v] = True

    for i in virus[v]:
        if not visited[i]:
            dfs(virus, i, visited)
    
    return visited.count(True) - 1


print(dfs(virus, 1, visited))