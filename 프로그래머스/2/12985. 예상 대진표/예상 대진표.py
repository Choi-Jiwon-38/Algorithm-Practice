def solution(n,a,b):
    answer = 1

    while abs(a - b) != 1 or min(a, b) % 2 != 1:
        a = a // 2 if a % 2 == 0 else (a + 1) // 2
        b = b // 2 if b % 2 == 0 else (b + 1) // 2
        answer += 1
    
    print(a, b)

    return answer
    
