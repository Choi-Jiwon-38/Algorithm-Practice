def solution(id_list, report, k):
    answer = []
    reports = dict()
    mail = dict()
    
    for id in id_list:
        reports[id] = []
        mail[id] = 0
    
    for text in report:
        u1, u2 = text.split(" ")
        if not u1 in reports[u2]:
            reports[u2].append(u1)
    
    for key in reports.keys():
        if len(reports[key]) >= k:
            for reporter_key in reports[key]:
                mail[reporter_key] += 1        
        
    for id in id_list:
        answer.append(mail[id])
        
    return answer 