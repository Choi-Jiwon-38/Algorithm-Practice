def solution(brown, yellow):
    # x * y = brown + yellow
    # 2 * x + 2 * y - 4 = brown

    for x in range(3, 2000):
        for y in range(1, x + 1):
            if x * y == brown + yellow and 2 * x + 2 * y - 4 == brown:
                return [x, y]
