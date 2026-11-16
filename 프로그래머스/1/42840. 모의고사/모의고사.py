

def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    results = []
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        answer = answers[i]
        
        if s1[i % len(s1)] == answer:
            scores[0] += 1
        
        if s2[i % len(s2)] == answer:
            scores[1] += 1
            
        if s3[i % len(s3)] == answer:
            scores[2] += 1
    
    max_score = max(scores)    
    
    for i in range(3):
        if scores[i] == max_score:
            results.append(i + 1)
    
    return results