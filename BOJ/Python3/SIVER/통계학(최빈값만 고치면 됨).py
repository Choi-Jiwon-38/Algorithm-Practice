# 백준 온라인 저지 2108번

import sys
input = sys.stdin.readline

n = int(input())
input_num = []
sum_num = 0

for _ in range(n):
    num = int(input())
    sum_num += num
    input_num.append(num)
    
print(input_num)
input_num.sort()
print(input_num)

def 산술평균():
    print(str(round(sum_num / n)))

def 중앙값():
    print(str(input_num[n//2]))

def 범위():
    print(str(input_num[n-1] - input_num[0]))

# 최빈값의 경우 cbg라는 변수에 담기로 한다.
mnc = 0
mnc_list = []
count = [0] * (input_num[n-1] + 1)

for i in input_num:
    if count[i] > mnc:
        mnc_list = []
        mnc = count[i]
        mnc_list.append(i)
    elif count[i] == mnc:
        mnc_list.append(i)
    else:
        pass

mnc_list.sort()
print(mnc_list)

if len(mnc_list) > 2:
    cbg = mnc_list[1]
else:
    cbg = mnc_list[0]

산술평균()
중앙값()
print(cbg)
범위()