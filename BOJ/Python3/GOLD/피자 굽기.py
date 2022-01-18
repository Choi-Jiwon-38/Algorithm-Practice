import sys
from tabnanny import check
input = sys.stdin.readline

D, N = map(int, input().split()) # D는 오븐의 깊이, N은 피자 반죽의 개수

depth_list = list(map(int, input().split()))
pizza_list = [0] * D

print(depth_list)
print(pizza_list)

check = 0

def pizza(r, check):
    check = 0

    for i in range(D):
        if i == 0:
            pass
        if i == 1:
            check = i

    
    for i in range(D):
        if depth_list[i] >= r:
            pizza_list[i] = 1
            break
        else:
            pizza_list[i] = -1


pizza(3)
pizza(2)
pizza(5)
print(pizza_list)