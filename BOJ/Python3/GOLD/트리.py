# 백준 알고리즘 저지
# 

import sys
input = sys.stdin.readline

n = int(input()) # 노드의 개수를 n에 저장
node_list = list(map(int, input().split())) # 각 노드의 부모를 node_list에 저장
node_num = int(input()) # 지우고 싶은 node의 번호를 node_num에 저장

def dfs(node_num, node_list):
    node_list[node_num] = -2 # 없앤 노드를 -2로 지정 (아무 곳에도 사용하지 않은 수)
    for i in range(n): # 노드 전체를 탐색하여 부모가 없어진 자식 노드도 제거
        if node_list[i] == node_num:
            dfs(i, node_list)

dfs(node_num, node_list)

count = 0
for i in range(len(node_list)):
    if node_list[i] != -2 and i not in node_list:
        count += 1

print(count)
