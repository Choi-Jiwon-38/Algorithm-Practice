# 백준 온라인 저지 1463번

num = int(input())
count = 0

while True:
    if num == 1:
        break
    if (num - 1) % 3 == 0:
        num -= 1
        count += 1

    if num % 3 == 0:
        num /= 3
        count += 1
    elif num % 2 == 0:
        num /= 2
        count += 1
    else:
        num -= 1
        count += 1


print(count)