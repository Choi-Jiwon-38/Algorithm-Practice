list_minus = []
list_plus = []
list_result = []

n = int(input())
for i in range(n):
    num = int(input())
    if num <= 0:
        list_minus.append(num)
    else:
        list_plus.append(num)

list_minus = sorted(list_minus)
list_plus = sorted(list_plus)

while len(list_minus) > 0:
    if len(list_minus) == 1:
        list_result.append(list_minus[0])
        del list_minus[0]
    else:
        mul_ = list_minus[0] * list_minus[1]
        list_result.append(mul_)
        del list_minus[0]
        del list_minus[0]
        


while len(list_plus) > 0:
    if len(list_plus) == 1:
        list_result.append(list_plus[0])
        del list_plus[0]
    else:
        sum_ = list_plus[len(list_plus)-1] + list_plus[len(list_plus)-2]
        mul_ = list_plus[len(list_plus)-1] * list_plus[len(list_plus)-2]
        if sum_ > mul_:
            list_result.append(sum_)
        else:
            list_result.append(mul_)
        list_plus.pop()
        list_plus.pop()

if len(list_result) == 2 and list_result[0] * list_result[1] == 0:
    print(0)
else:
    print(sum(list_result))