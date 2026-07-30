import heapq

def solution(scoville, K):
    hq = []
    
    for s in scoville:
        heapq.heappush(hq, s)
    
    flag = True if hq[0] >= K else False
    count = 0
    
    while not flag and len(hq) >= 2:
        count += 1
        x1, x2 = heapq.heappop(hq), heapq.heappop(hq)
        x3 = x1 + x2 * 2
        
        heapq.heappush(hq, x3)
        
        if hq[0] >= K:
            flag = True
        
    return count if flag else -1