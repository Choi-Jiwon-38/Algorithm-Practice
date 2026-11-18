def get_rank(count):
    if count < 2:
        return 6
    
    return 7 - count


def solution(lottos, win_nums):
    win_count = 0
    unknown_count = lottos.count(0)
    
    for lotto in lottos:
        if lotto in win_nums:
            win_count += 1
    
    answer = [get_rank(win_count + unknown_count), get_rank(win_count)]
    
    return answer