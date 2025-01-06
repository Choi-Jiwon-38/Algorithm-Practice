import math

def count_of_divisors(n, limit, power):
    count = 0
    
    if n == 1:
        return 1
    
    for i in range(1, int(n ** 0.5) + 1):
        if i * i == n:
            count += 1
        elif n % i == 0:
            count += 2
    
    return power if count > limit else count

def solution(number, limit, power):
    answer = 0
    
    list = []
    
    for n in range(1, number + 1):
        list.append(count_of_divisors(n, limit, power))
            
    return sum(list)