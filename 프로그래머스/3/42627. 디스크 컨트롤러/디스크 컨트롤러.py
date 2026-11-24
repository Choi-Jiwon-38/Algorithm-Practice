import heapq
from collections import deque

def solution(jobs):
    jobs.sort()
    jobs = deque(jobs)
    answers = []
    n = len(jobs)
    hq = []
    
    time = 0
    idx = 0
    
    while len(answers) < n:
        # time 기준으로 힙에 넣을 수 있는 항목 넣기
        while jobs and time >= jobs[0][0]:
            job = jobs.popleft()
            heapq.heappush(hq, (job[1], job[0], idx))
            idx += 1
        
        # 지금 힙에서 뺄 수 있는 거 빼기
        if hq:
            ut, rt, _ = heapq.heappop(hq)
        
            time += ut
            rtt = time - rt
            
            answers.append(rtt)
        
        
        if not hq and jobs and time < jobs[0][0]:
            time = jobs[0][0]

    return sum(answers) // len(answers)