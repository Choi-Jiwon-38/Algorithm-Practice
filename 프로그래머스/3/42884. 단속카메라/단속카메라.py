def solution(routes):
    routes.sort()
    answer = 1
    curr_start = routes[0][0]
    curr_end = routes[0][1]
    
    for i in range(1, len(routes)):
        if curr_start <= routes[i][0] <= curr_end:
            curr_start = max(curr_start, routes[i][0])
            curr_end = min(curr_end, routes[i][1])
            continue
        else:
            curr_start = routes[i][0]
            curr_end = routes[i][1]
            answer += 1
    
    return answer