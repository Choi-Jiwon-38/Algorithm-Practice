def solution(data, ext, val_ext, sort_by):
    answer = []
    
    index_map = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }
    
    for raw_data in data:
        if raw_data[index_map[ext]] < val_ext:
            answer.append(raw_data)
    
    answer.sort(key=lambda x: x[index_map[sort_by]]) 
    
    return answer