# 백준 온라인 저지 1924번

x, y = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

day = 0

for i in range(12):
    if i < x-1:
        day += month[i]

day += y

print(answer[day%7])
