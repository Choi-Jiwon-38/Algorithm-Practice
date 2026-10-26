def convert_time_to_int(str_time):
    h, m = map(int, str_time.split(":"))
    return h * 60 + m

def next(pos, max):
    return min(pos + 10, max)

def prev(pos):
    return max(pos - 10, 0)

def skip_op(pos, op_start, op_end):
    if op_start <= pos <= op_end:
        return op_end
    return pos

def convert_to_answer(pos):
    h = pos // 60
    
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)
        
    m = pos % 60
    
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    
    return h + ':' + m
    

def solution(video_len, pos, op_start, op_end, commands):
    video_len = convert_time_to_int(video_len)
    pos = convert_time_to_int(pos)
    op_start = convert_time_to_int(op_start)
    op_end = convert_time_to_int(op_end)

    for command in commands:
        pos = skip_op(pos, op_start, op_end)
        
        if command == 'next':
            pos = next(pos, video_len)
        elif command == 'prev':
            pos = prev(pos)
            
        pos = skip_op(pos, op_start, op_end)
        
    answer = convert_to_answer(pos)
    return answer