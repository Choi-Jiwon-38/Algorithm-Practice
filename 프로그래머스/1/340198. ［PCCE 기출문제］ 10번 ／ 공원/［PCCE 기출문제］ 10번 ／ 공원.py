def solution(mats, park):
    answer = -1
    max_y = len(park)
    max_x = len(park[0])
    
    for i in range(max_y):
        for j in range(max_x):
            for mat in mats:
                if answer >= mat:
                    continue
                else:
                    if check(i, j, max_y, max_x, mat, park):
                        answer = mat
    
    return answer

def check(y, x, max_y, max_x, size, park):
    if y + size > max_y or x + size > max_x:
        return False
    
    for i in range(size):
        for j in range(size):
            if park[y + i][x + j] != '-1':
                return False
    
    return True

