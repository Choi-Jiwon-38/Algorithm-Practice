def solution(id_list, report, k):
    answer = []
    report_dict = dict()
    id_dict = dict()
    
    for id in id_list:
        report_dict[id] = set()
        id_dict[id] = set()
        
    # dict 초기화
    for r in report:
        user_id, reported_id = r.split(" ")
        report_dict[reported_id].add(user_id)
        id_dict[user_id].add(reported_id)
        
            
    for id in id_list:
        count = 0
        
        for i in id_dict[id]:
            if len(report_dict[i]) >= k:
                count += 1
        
        answer.append(count)
    
    
    return answer