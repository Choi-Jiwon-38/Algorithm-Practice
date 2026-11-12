# cmp_to_key 사용 방법 익히기
from functools import cmp_to_key

def compare(x1, x2):
    n1 = x1 + x2
    n2 = x2 + x1
    
    if n1 > n2:
        return -1
    else:
        return 1

def solution(numbers):
    str_nums = [str(num) for num in numbers]
    str_nums.sort(key=cmp_to_key(compare))

    answer = ''.join(str_nums)
    
    # [0, 0] 이런 식으로 들어왔을 때, 처리
    if answer[:2] == '00':
        answer = '0'
    
    return answer
