from collections import deque
import math

def solution(progresses, speeds):
    task_queue = deque()
    answer = []
    
    for i in range(len(progresses)):
        task_queue.append([progresses[i], speeds[i]])
    
    # task queue가 비어있지 않는 동안(작업이 모두 완료될때까지)
    while len(task_queue):        
        rest = math.ceil((100 - task_queue[0][0]) / task_queue[0][1])
        cnt = 0
        
        while (len(task_queue) and task_queue[0][0] + rest * task_queue[0][1] >= 100):
            cnt += 1
            task_queue.popleft()
        
        answer.append(cnt)

    return answer