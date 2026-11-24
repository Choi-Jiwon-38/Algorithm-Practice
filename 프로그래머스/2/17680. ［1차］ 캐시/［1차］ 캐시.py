from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    q = deque([])
    
    if cacheSize == 0:
        return len(cities) * 5
    
    
    for city in cities:
        city = city.upper() # 대소문자 구별을 안하므로 한쪽으로 변환
        
        if city in q: # hit
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            if len(q) < cacheSize:
                q.append(city)
            else:
                q.popleft()
                q.append(city)
                
    return answer