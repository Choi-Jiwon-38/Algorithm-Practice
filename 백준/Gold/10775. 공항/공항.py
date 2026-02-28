import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

g = int(input())
p = int(input())

planes = []

for _ in range(p):
    planes.append(int(input()))

parent = [i for i in range(g+1)]

def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(rootA, rootB):
    parent[rootB] = rootA

answer = 0

for plane in planes:
    x = find(plane) # plane 이하에서 가능한 최대 게이트
    if x == 0:
        break
    answer += 1
    union(x-1, x)
    
print(answer)