# 벡준 온라인 저지 9733번
# 참고 사이트 :: https://blog.naver.com/redtaeung/221906225810 (EOF 처리 방법)

workNameList = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
workCounter = [0, 0, 0, 0, 0, 0, 0]
beeWorkList = []
totalWork = 0

while True: # 입력이 끝날 때까지 출력 (EOF 처리) <--- Error 해결
    try:
        temp = list(input().split())
        beeWorkList += temp
    except:
        break

for w in beeWorkList: # 주어진 목록에 있는 일의 경우
    if w == 'Re':
        workCounter[0] += 1
    elif w == 'Pt':
        workCounter[1] += 1
    elif w == 'Cc':
        workCounter[2] += 1
    elif w == 'Ea':
        workCounter[3] += 1
    elif w == 'Tb':
        workCounter[4] += 1
    elif w == 'Cm':
        workCounter[5] += 1
    elif w == 'Ex':
        workCounter[6] += 1
    else:
        pass
    totalWork += 1 # 주어진 목록에 있는 일 + 없는 일 모두 카운트

for i in range(7):
    rate = workCounter[i]/totalWork
    print(workNameList[i], workCounter[i], end=' ')
    print(f'{rate:.2f}')
print(f'Total {totalWork} 1.00')