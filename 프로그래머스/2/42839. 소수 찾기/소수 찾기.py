def count_prime_number(n, number_set):
    is_prime = [True for _ in range(n + 1)]
    
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, int(n ** 0.5)):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    
    count = 0
    
    for number in number_set:
        if is_prime[number]:
            count += 1
    
    return count
    

def make_numbers(n, curr, number_set, numbers, used):
    for i in range(n):
        if not used[i]:
            used[i] = True
            number_set.add(int(curr + numbers[i]))
            make_numbers(n, curr + numbers[i], number_set, numbers, used)
            used[i] = False

def solution(numbers):    
    number_set = set()
    n = len(numbers)
    used = [False for _ in range(n)]
    
    make_numbers(n, '', number_set, numbers, used)
    
    max_number = max(number_set)
    
    answer = count_prime_number(max_number, number_set)
    
    
    return answer