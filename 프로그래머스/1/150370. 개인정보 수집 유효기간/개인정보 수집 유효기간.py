def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split('.'))
    
    term_dict = dict()
    answer = []
    
    for term in terms:
        key, value = term.split()
        term_dict[key] = int(value) * 28
    
    for i in range(len(privacies)):
        privacy = privacies[i]
        date, term = privacy.split()
        y, m, d = map(int, date.split('.'))
        
        d += term_dict[term] - 1
        
        # day -> extra month + day로 조정
        extra_m = d // 28
        m += extra_m - 1 if d % 28 == 0 else extra_m
        d = 28 if d % 28 == 0 else d % 28
        
        # month -> extra year + month로 조정
        extra_y = m // 12
        y += extra_y - 1 if m % 12 == 0 else extra_y
        m = 12 if m % 12 == 0 else m % 12
        
        if y < ty:
            answer.append(i + 1)
        elif y == ty:
            if m < tm:
                answer.append(i + 1)
            elif m == tm:
                if d < td:
                    answer.append(i + 1)
        
    
    return answer