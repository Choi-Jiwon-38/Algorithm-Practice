def solution(n, words):
    used_words = dict()
    used_words[words[0]] = True
    
    for i in range(1, len(words)):
        curr = words[i]
        prev = words[i - 1]
        
        if curr in used_words or prev[-1] != curr[0]:
            user = n if (i + 1) % n == 0 else (i + 1) % n
            step = (i + 1) // n + 1 if (i + 1) % n != 0 else (i + 1) // n
            
            return [user, step]
        else:
            used_words[curr] = True
        
    return [0, 0]