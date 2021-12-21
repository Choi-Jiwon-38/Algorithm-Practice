# 입력받은 정수의 부호(양수, 음수. 0) 출력하기

n = int(input('정수를 입력하세요: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')



# 3개로 분기하는 조건문

n = int(input('정수를 입력하세요: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
else:
    print('C')



# 4개로 분기하는 조건문

n = int(input('정수를 입력하세요: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')


# 바로 위 코드와 동치

n = int(input('정수를 입력하세요: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
else:
    pass