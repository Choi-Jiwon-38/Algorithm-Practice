import heapq
from collections import deque

def solution(jobs):
    disk_q = []
    time = 0
    index = 0
    answer = 0
    jobs.sort() # 작업 요청 시간이 빠른 순으로 정렬
    
    while index < len(jobs) or disk_q:
        
        while index < len(jobs) and jobs[index][0] <= time:
            # 소요 시간이 짧은 것 -> 요청 시각이 빠른 것 -> 작업의 번호가 작은 것
            heapq.heappush(disk_q, (jobs[index][1], jobs[index][0], index))
            index += 1
        
        if disk_q:
            disk = heapq.heappop(disk_q)
            time += disk[0]
            answer += time - disk[1]     
            
        else: # 프로세스 큐가 비어있는 경우
            time += 1

    return answer // len(jobs)
            