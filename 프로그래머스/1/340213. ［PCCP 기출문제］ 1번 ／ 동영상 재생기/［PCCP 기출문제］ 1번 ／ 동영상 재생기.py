

def convert_time_to_num(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def convert_num_to_time(time):
    hours = str(time // 60)
    minutes = str(time % 60)
    
    # 빈 자리수만큼 0 채우는 방법이 있는 것으로 알고 있음.
    if len(hours) == 1:
        hours = '0' + hours  

    if len(minutes) == 1:
        minutes = '0' + minutes
    
    return hours + ':' + minutes


def move_to_prev(time):
    time = time - 10  
    
    if time < 10:
        return 0
    else:
        return time

def move_to_next(time, end_time):
    time = time + 10
    
    if end_time - time < 10:
        return end_time
    else:
        return time

def skip_if_op(time, op_start_time, op_end_time):
    if op_start_time <= time and time <= op_end_time:
        return op_end_time
    else:
        return time
    
def solution(video_len, pos, op_start, op_end, commands):    
    curr_time = convert_time_to_num(pos)
    op_start_time = convert_time_to_num(op_start)
    op_end_time = convert_time_to_num(op_end)
    end_time = convert_time_to_num(video_len)
    
    if op_start_time <= curr_time and curr_time <= op_end_time:
        curr_time = op_end_time
    
    
    for command in commands:
        if command == 'next':
            curr_time = move_to_next(curr_time, end_time)
        elif command == 'prev':
            curr_time = move_to_prev(curr_time)
    
        curr_time = skip_if_op(curr_time, op_start_time, op_end_time)
    
    return convert_num_to_time(curr_time)