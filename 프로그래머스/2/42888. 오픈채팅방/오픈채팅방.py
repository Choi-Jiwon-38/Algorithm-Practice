def solution(record):
    users = dict()
    
    # users dict 갱신
    for r in record:
        cmds = list(r.split(" "))
        
        if cmds[0] == 'Enter' or cmds[0] == 'Change':
            users[cmds[1]] = cmds[2]
        else: # Leave - 닉네임 변경에 영향이 없음
            continue
            
    # 채팅방 메시지 갱신
    answer = []
    
    for r in record:
        cmds = list(r.split(" "))
        
        if cmds[0] == 'Enter':
            answer.append(f'{users[cmds[1]]}님이 들어왔습니다.')
        elif cmds[0] == 'Leave':
            answer.append(f'{users[cmds[1]]}님이 나갔습니다.')
    
    
    return answer