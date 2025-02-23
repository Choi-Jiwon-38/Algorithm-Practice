def solution(sizes):
    max_w = 0
    max_h = 0
    
    for size in sizes:
        # 명함 회전 X
        max_w1 = max(max_w, size[0])
        max_h1 = max(max_h, size[1])
        
        # 명함 회전 O
        max_w2 = max(max_w, size[1])
        max_h2 = max(max_h, size[0])
        
        if max_w2 * max_h2 > max_w1 * max_h1:
            max_w, max_h = max_w1, max_h1
        else:
            max_w, max_h = max_w2, max_h2
        
    return max_w * max_h