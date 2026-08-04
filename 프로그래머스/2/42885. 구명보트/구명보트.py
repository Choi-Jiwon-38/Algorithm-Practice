def solution(people, limit):
    people.sort()
    
    l = len(people)
    i = 0
    j = l - 1
    
    answer = 0
    
    while i <= j:
        if people[i] + people[j] > limit:
            j -= 1
            answer += 1
        else:
            answer += 1
            i += 1
            j -= 1
        
    return answer