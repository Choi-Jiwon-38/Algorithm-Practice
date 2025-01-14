import heapq

def solution(scoville, K):
    answer = 0
    hq = scoville
    heapq.heapify(hq)
    
    while hq[0] < K: # 가진 음식의 스코빌 지수가 K보다 작은 경우에는 반복
        if len(hq) > 1:
            answer += 1
            first = heapq.heappop(hq)
            second = heapq.heappop(hq)

            new = first + second * 2
            heapq.heappush(hq, new)
        else:
            break

    return answer if hq[0] >= K else -1
