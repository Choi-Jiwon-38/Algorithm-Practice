def solution(sizes):
    max_x = 0
    max_y = 0
    
    for curr_x, curr_y in sizes:
        # 정방향
        size1 = max(max_x, curr_x) * max(max_y, curr_y)
        # 회전
        size2 = max(max_x, curr_y) * max(max_y, curr_x)
    
        if size1 < size2:
            max_x = max(max_x, curr_x)
            max_y = max(max_y, curr_y)
        else: 
            max_x = max(max_x, curr_y)
            max_y = max(max_y, curr_x)
            
    return max_x * max_y