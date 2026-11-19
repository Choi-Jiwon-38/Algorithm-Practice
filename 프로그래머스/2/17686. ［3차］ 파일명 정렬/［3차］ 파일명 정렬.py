def solution(files):
    file_dict = dict()
    
    for idx in range(len(files)):
        arr = []
        file = files[idx]
        i = 0
        max_idx = len(file)
        
        # HEAD 구하기
        while i < max_idx and not ('0' <= file[i] <= '9'):
            i += 1
        
        arr.append(file[:i].upper()) # 대소문자 구분을 하지 않으므로 upper, lower 중 택 1 수행
        
        # NUMBER 구하기
        number_start_idx = i
        count = 0
        
        while i < max_idx and '0' <= file[i] <= '9' and count < 5:
            count += 1
            i += 1
        
        arr.append(file[number_start_idx:i])
        
        # TAIL 구하기
        # TAIL은 정렬에 관여하지 않고, 입력 순서를 유지해야 하므로 index를 arr에 추가
        arr.append(idx)
        
        file_dict[file] = arr
        
    
    files.sort(key=lambda x: (file_dict[x][0], int(file_dict[x][1]), file_dict[x][2]))
    
    return files