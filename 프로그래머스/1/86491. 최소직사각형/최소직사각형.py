def solution(sizes):
    wallet_x = sizes[0][0]
    wallet_y = sizes[0][1]
    
    for i in range(1, len(sizes)):
        x, y = sizes[i]
        
        if (x <= wallet_x and y <= wallet_y) or (y <= wallet_x and x <= wallet_y):
            continue
        
        if max(x, wallet_x) * max(y, wallet_y) < max(y, wallet_x) * max(x, wallet_y):
            wallet_x = max(x, wallet_x)
            wallet_y = max(y, wallet_y)
        else:
            wallet_x = max(y, wallet_x)
            wallet_y = max(x, wallet_y)
    
    return wallet_x * wallet_y