def solution(want, number, discount):
    want_dict = dict()
    answer = 0
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    start_idx = 0
    end_idx = 9

    for i in range(10):
        if discount[i] in want_dict:
            want_dict[discount[i]] -= 1

    
    def check_all_sale():
        is_all_sale = True
        
        for v in want_dict.values():            
            if v > 0:
                is_all_sale = False
                break
        
        return is_all_sale
    
    if check_all_sale():
        answer += 1

        
    while end_idx < len(discount) - 1: 
        if discount[start_idx] in want_dict: want_dict[discount[start_idx]] += 1
        start_idx += 1
        end_idx += 1
        if discount[end_idx] in want_dict: want_dict[discount[end_idx]] -= 1
        
        if check_all_sale(): answer += 1
    
    return answer