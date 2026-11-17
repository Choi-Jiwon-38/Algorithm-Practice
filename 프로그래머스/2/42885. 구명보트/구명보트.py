def solution(people, limit):
    # 구명보트 개수
    answer = 0
    
    people.sort()
    
    i = 0
    j = len(people) - 1
    
    while i <= j:
        if i == j:
            answer += 1
            break
        
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        
        answer += 1
    

    return answer