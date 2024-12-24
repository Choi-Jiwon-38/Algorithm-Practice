def solution(brown, yellow):
    
    for i in range(1, yellow + 1):
        if yellow % i != 0:
            continue
        x, y = i, yellow // i
        
        print(x, y)
        
        if brown == 2 * (x + y) + 4:
            return [y + 2, x + 2]
        
        