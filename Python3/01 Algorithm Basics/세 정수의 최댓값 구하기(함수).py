# 세 정수의 최댓값 구하기(함수)

def max3(a, b, c):
    """a, b, c의 최댓값을 구하여 반환"""
    maximum = a
    if maximum < b: maximum = b
    if maximum < c: maximum = c
    
    return maximum

print(f'max3(10, 50, 34) = {max3(10, 50, 34)}')