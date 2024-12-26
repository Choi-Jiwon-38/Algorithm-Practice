def solution(people, limit):
    # two pointer와 greedy 이용
    people.sort()
    
    answer = 0
    
    i = 0
    j = len(people) - 1
    
    while i <= j:
        if people[i] + people[j] <= limit: # 남은 인원 중 가장 가벼운 사람과 가장 무거운 사람이 같이 타는 경우
            i += 1 # 가벼운 사람을 태움
            j -= 1 # 무거운 사람을 태움
            answer += 1 # 배 1척 소모
        else: # 못타는 경우에는 무거운 사람때문에 타지 못한 것임
            j -= 1 # 무거운 사람을 태움
            answer += 1 # 배 1척 소모

    return answer