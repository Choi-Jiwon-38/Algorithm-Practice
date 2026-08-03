from collections import deque
import math

def solution(fees, records):
    bt, bf, ut, uf = fees
    park = dict()
    fee = dict()
    
    
    for record in records:
        t, cn, cmd = record.split()
    
        h, m = map(int, t.split(":"))
        total_time = h * 60 + m
        
        if cn in park:
            park[cn].append(total_time)
        else:
            park[cn] = deque([total_time])
    
    
    park_keys = park.keys()
    
    for pk in park_keys:
        if len(park[pk]) % 2 != 0:
            park[pk].append(23 * 60 + 59)
    
    for pk in park_keys:
        park_time = 0
        park_fee = 0
        
        while park[pk]:
            in_time, out_time = park[pk].popleft(), park[pk].popleft()
            park_time += out_time - in_time

        # 기본 주차시간 추가 및 비용 부과
        park_time -= bt
        park_fee += bf
        
        print(park_time, park_fee)
        
        if park_time > 0:
            park_fee += math.ceil(park_time / ut) * uf
        
        fee[pk] = park_fee
    
    answer = []
    
    fee_keys = list(fee.keys())
    fee_keys.sort()
    
    for fk in fee_keys:
        answer.append(fee[fk])
    
    return answer