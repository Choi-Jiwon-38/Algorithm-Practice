def solution(brown, yellow):
    for y in range(5000):
        for x in range(y, 5000):
            if 2 * y + 2 * x + 4 == brown and x * y  == yellow:
                return [x + 2, y + 2]

    return answer