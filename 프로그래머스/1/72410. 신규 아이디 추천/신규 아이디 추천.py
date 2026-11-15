def solution(new_id):
    # step 1
    new_id = new_id.lower()
    

    
    # step 2
    tmp = ''
    for c in new_id:

        
        if 'a' <= c <= 'z' or c == '-' or c == '_' or c == '.' or '0' <= c <= '9':
            tmp += c
    
    new_id = tmp

    
    # step 3
    flag = False
    
    tmp = ''
    for c in new_id:
        if tmp and tmp[-1] == '.' and c == '.':
            continue
        else:
            tmp += c
    
    new_id = tmp

    # step 4
    tmp = ''
    
    for i in range(len(new_id)):
        if i == 0 or i == len(new_id) - 1:
            if new_id[i] != '.':
                tmp += new_id[i]
        else:
            tmp += new_id[i]
    
    new_id = tmp
   
    # step 5
    if new_id == '':
        new_id = 'a'

   
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
        if new_id[-1] == '.':
            new_id = new_id[:14]
    
    # step 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
 
    return new_id