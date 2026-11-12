import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        s1 = heapq.heappop(scoville)
        
        if s1 >= K:
            return answer
        
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + s2 * 2)
        answer += 1
    
    if scoville[0] >= K:
        return answer
    else:
        return -1