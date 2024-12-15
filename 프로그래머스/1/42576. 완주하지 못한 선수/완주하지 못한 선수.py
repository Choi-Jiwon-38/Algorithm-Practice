def solution(participant, completion):
    participant.sort()
    completion.sort()

    total = len(participant)
    
    for i in range(total - 1):
        if (participant[i] != completion[i]):
            return participant[i]
    
    # 리스트의 마지막 원소에 해당하는 선수가 완주하지 못한 경우 return
    return participant[total - 1]