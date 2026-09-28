def solve(y, x, size, arr, result):
    count0 = 0
    count1 = 0
    
    totalCount0 = result[0]
    totalCount1 = result[1]
    
    for i in range(size):
        for j in range(size):
            cy = y + i
            cx = x + j
            
            if arr[cy][cx] == 0:
                count0 += 1
            else:
                count1 += 1
            
    if count0 == size ** 2:
        totalCount0 += 1
        return [totalCount0, totalCount1]

    if count1 == size ** 2:
        totalCount1 += 1
        return [totalCount0, totalCount1]
    
    half = size // 2
    
    for ny, nx in [(y, x), (y, x + half), (y + half, x), (y + half, x + half)]:
        totalCount0, totalCount1 = solve(ny, nx, half, arr, [totalCount0, totalCount1])
    
    return [totalCount0, totalCount1]


def solution(arr):
    return solve(0, 0, len(arr), arr, [0, 0])