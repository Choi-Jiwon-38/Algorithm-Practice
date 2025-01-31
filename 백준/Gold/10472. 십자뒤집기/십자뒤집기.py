import sys
from collections import deque
input = sys.stdin.readline
import copy

def click(board, i, j):
    new_board = copy.deepcopy(board)
    new_board[i][j] ^= 1

    if i > 0:
        new_board[i - 1][j] ^= 1
    if i < 2:
        new_board[i + 1][j] ^= 1
    if j > 0:
        new_board[i][j - 1] ^= 1
    if j < 2:
        new_board[i][j + 1] ^= 1

    return new_board

def bfs(board, target):
    q = deque([(board, 0)])
    visit = set()
    visit.add(tuple(map(tuple, board))) 

    while len(q):
        curr_board, depth = q.popleft()

        if curr_board == target:
            print(depth)
            return
        
        for i in range(3):
            for j in range(3):
                next_board = click(curr_board, i, j)
                next_board_tuple = tuple(map(tuple, next_board))
                
                if next_board_tuple not in visit:
                    visit.add(next_board_tuple)
                    q.append((next_board, depth + 1))
                
t = int(input().rstrip())

for _ in range(t):
    target = [] 
    for _ in range(3):
        row = input().rstrip()
        target.append([1 if r == '*' else 0 for r in row])

    board = [[0] * 3 for _ in range(3)] 
    bfs(board, target)
