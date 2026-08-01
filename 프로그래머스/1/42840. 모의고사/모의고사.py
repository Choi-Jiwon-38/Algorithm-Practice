def solution(answers):
    answer = []
    
    solution = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    score = [0, 0, 0]
    
    
    for i in range(len(answers)):
        curr_answer = answers[i]
        for j in range(3):
            curr_solution = solution[j]
            if curr_solution[i % len(curr_solution)] == curr_answer:
                score[j] += 1
    
    max_score = max(score)
    
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)
    
    return answer