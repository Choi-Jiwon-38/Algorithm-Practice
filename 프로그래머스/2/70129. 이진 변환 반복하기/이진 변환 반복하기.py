def solution(s):
    step = 0    # 이진 변환 수행 횟수
    count = 0   # 0 제거 횟수
    
    while s != '1':
        zero_count = s.count('0')
        c = len(s) - zero_count
        
        count += zero_count
        
        s = bin(c)[2:]
        step += 1
        
    return [step, count]