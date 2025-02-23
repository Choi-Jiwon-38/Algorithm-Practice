def solution(answers):
    score = [0, 0, 0]
    
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len1, len2, len3 = 5, 8, 10
    
    
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len1]:
            score[0] += 1
        
        if answers[i] == pattern2[i % len2]:
            score[1] += 1
        
        if answers[i] == pattern3[i % len3]:
            score[2] += 1
        
    max_score = max(score)
    answer = []
    
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)
    
    return answer