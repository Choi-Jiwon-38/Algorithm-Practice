import heapq

def solution(operations):
    min_h = []
    max_h = []
    length = 0
    
    for operation in operations:
        cmd, num = operation.split(" ")        
        
        if cmd == 'I':
            heapq.heappush(min_h, int(num))
            heapq.heappush(max_h, -int(num))
            length += 1
        else: # cmd == 'D'
            if length > 0:
                if num == '1':
                    heapq.heappop(max_h)
                    min_h = sorted(min_h)[:-1]
                else: # num == '-1'
                    heapq.heappop(min_h)
                    max_h = sorted(max_h)[:-1]
                length -= 1
    
    # 이중 우선순위 큐가 비어있는 경우에는 [0, 0]을 반환
    return [0, 0] if length < 1 else [-heapq.heappop(max_h), heapq.heappop(min_h)] 