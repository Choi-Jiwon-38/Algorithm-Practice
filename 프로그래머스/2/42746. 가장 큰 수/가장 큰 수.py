from functools import cmp_to_key

def compare(n1, n2):
    return int(str(n1) + str(n2)) - int(str(n2) + str(n1))

def solution(numbers):
    numbers.sort(key=cmp_to_key(compare))
    answer = ''
    
    for n in numbers:
        answer = str(n) + answer
    
    return '0' if answer[0] == '0' else answer