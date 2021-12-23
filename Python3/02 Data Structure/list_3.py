# 리스트의 모든 원소를 스캔하기(enumerate() 함수 이용)

x = ['A', 'B', 'C', 'D']

for i, name in enumerate(x, 1): # 1부터 카운트
    print(i, name)

for i, name in enumerate(x, 2): # 2부터 카운트
    print(i, name)