x = ' ' + input().rstrip()
y = ' ' + input().rstrip()
board = [[0] * len(y) for _ in range(len(x))]

for i in range(1, len(x)):
    for j in range(1, len(y)):
        if x[i] == y[j]:
            board[i][j] = board[i-1][j-1] + 1
        else:
            if board[i-1][j] > board[i][j-1]:
                board[i][j] = board[i-1][j]
            else:
                board[i][j] = board[i][j-1]


print(board[-1][-1])