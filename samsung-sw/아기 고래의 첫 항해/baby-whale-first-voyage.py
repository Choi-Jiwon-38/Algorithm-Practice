from collections import deque

# n: 격자 크기
# r: 고래 시작 위치(행)
# c: 고래 시작 위치(열)
# d: 고래 초기 방향(1 상, 2 하, 3좌, 4 우)
n, r, c, d = map(int, input().split())

# 이동
# type 0: 현재 바라보는 방향으로 직진
# type 1: 좌회전 후 직진
# type 2: 우회전 후 직진
# type 3: 180도 회전 후 직진
def move(d, r, c, type):
    if type == 0:
        if d == 1:
            return d, r - 1, c
        elif d == 2:
            return d, r + 1, c
        elif d == 3:
            return d, r, c - 1
        else: # d == 4
            return d, r, c + 1
    elif type == 1:
        if d == 1:
            return 3, r, c - 1
        elif d == 2:
            return 4, r, c + 1
        elif d == 3:
            return 2, r + 1 , c
        else: # d == 4
            return 1, r - 1, c
    elif type == 2:
        if d == 1:
            return 4, r, c + 1
        elif d == 2:
            return 3, r, c - 1
        elif d == 3:
            return 1, r - 1, c
        else: # d == 4
            return 2, r + 1, c
    elif type == 3:
        if d == 1:
            return  2, r + 1, c
        elif d == 2:
            return 1, r - 1, c
        elif d == 3:
            return 4, r, c + 1
        else: # d == 4
            return 3, r, c - 1

maps = []

# 헤엄칠 수 있는 바다 칸의 개수(입력에서 업데이트)
k = 0

# 찾은 바다 칸의 개수(고래는 바다 칸에 있으므로 1)
found = 1
# travel 2의 visited 방문용 + travel 1의 바다 칸 방문용
step = 1

for i in range(n):
    col = list(map(int, input().split()))
    k += col.count(0)
    maps.append(col)

def travel1(d, r, c):
    global found
    cd, cr, cc = d, r, c
    flag = True

    while flag:
        flag = False

        for type in range(4):
            nd, nr, nc = move(cd, cr, cc, type)

            if 0 <= nr and nr < n and 0 <= nc and nc < n and maps[nr][nc] == 0:
                # 갱신
                cd, cr, cc = nd, nr, nc
                print(nr + 1, nc + 1)
                found += 1
                maps[nr][nc] = -1 
                flag = True
                break
    
    # 현재 방향, 행, 열 정보 반환
    return cd, cr, cc 


def travel2(d, r, c):
    global found

    maps[r][c] = -step
    
    q = deque([(d, r, c, 0)])
    
    next_pos = []

    min_dist = 99999

    while q:
        cd, cr, cc, cdist = q.popleft()
    
        if cdist + 1 > min_dist:
            continue

        # 좌-하-우-상
        for nd, dr, dc in [(3, 0, -1), (2, 1, 0), (4, 0, 1), (1, -1, 0)]:
            nr, nc = cr + dr, cc + dc 
            ndist = cdist + 1

            if 0 <= nr and nr < n and 0 <= nc and nc < n and maps[nr][nc] != 1 and -step != maps[nr][nc]:
                if maps[nr][nc] == 0:
                    min_dist = ndist
                    # 확인 필요: 후보는 방문 처리를 하면 안됨
                    next_pos.append((nd, nr, nc))
                else:
                    maps[nr][nc] = -step
                    q.append((nd, nr, nc, ndist))

    next_pos.sort(key=lambda x: (x[1], x[2]))
    nd, nr, nc = next_pos[0]

    found += 1
    maps[nr][nc] = -step
    print(nr + 1, nc + 1)

    return nd, nr, nc

cd, cr, cc = d, r - 1, c - 1
maps[cr][cc] = -step
print(r, c)

while found < k:
    cd, cr, cc = travel1(cd, cr, cc)
    step += 1
    if found < k:
        cd, cr, cc = travel2(cd, cr, cc)