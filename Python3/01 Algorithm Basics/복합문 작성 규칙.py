# 복합문의 스위트는 반드시 행마다 같은 수준으로 들여쓰기
a = 1
b = 2

if a < b:
    min2 = a
    max2 = b


# 스위트가 단순문인 경우, 헤더와 같은 행에 둘 수 있음
if a < b: min2 = a  # 단순문 1개
if a < b: min2 = a; max2 = b # 단순문 2개
if a < b: min2 = a; max2 = b; # 단수문 2개(세미콜론 추가)

# 스위트가 복합문인 경우, 헤더와 같은 행에 둘 수 없음(Error)
# if a < b: if b > a: max2 = a