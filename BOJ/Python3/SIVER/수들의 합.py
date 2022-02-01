
S = int(input())
count = 0
num = 1

while 1:
    S -= num
    if S < 0:
        break
    count += 1
    num += 1

print(count)