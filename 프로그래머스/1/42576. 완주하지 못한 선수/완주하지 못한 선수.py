def solution(participant, completion):
    runners = {}
    
    for p in participant:
        if p in runners:
            runners[p] += 1
        else:
            runners[p] = 1
            
    for c in completion:
        runners[c] -= 1
        if runners[c] == 0:
            del runners[c]
            
    return list(runners.keys())[0]
    
    
            