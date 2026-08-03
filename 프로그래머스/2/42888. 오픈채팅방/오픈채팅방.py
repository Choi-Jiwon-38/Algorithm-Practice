def solution(record):
    name_dict = dict()
    answer = []
    
    for r in record:
        command = r.split(" ")
        
        if command[0] == 'Enter' or command[0] == 'Change':
            name_dict[command[1]] = command[2] 
            
    for r in record:
        command = r.split(" ")
        
        if command[0] == 'Enter':
            answer.append(name_dict[command[1]] + '님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(name_dict[command[1]] + '님이 나갔습니다.')
            
    return answer