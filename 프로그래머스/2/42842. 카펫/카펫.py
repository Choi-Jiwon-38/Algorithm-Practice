def solution(brown, yellow):
    for x in range(1, yellow + 1):
        if yellow % x == 0:
            y = yellow / x
        
            if brown == 2 * (x + y) + 4:
                return [x + 2, y + 2] if x >= y else [y + 2, x + 2]