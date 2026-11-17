def solution(N, stages):
    fail = [0 for _ in range(N + 2)]
    fail_rate = [0 for _ in range(N + 1)]
    
    for stage in stages:
        fail[stage] += 1
    
    survived_user_count = len(stages)
    
    for i in range(N + 1):
        if fail[i] != 0:
            fail_rate[i] = fail[i] / survived_user_count
            survived_user_count -= fail[i] 
    
    answer = [i for i in range(1, N + 1)]
    answer.sort(key=lambda x: (-fail_rate[x], x))
    
    return answer