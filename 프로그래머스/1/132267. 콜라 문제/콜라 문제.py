import math

def solution(a, b, n):
    answer = 0
    
    while True:
        bundle = math.floor(n / a)
        use = bundle * a
        get = bundle * b

        n = n - use + get
        
        answer += get
        if get < 1:
            break


    return answer