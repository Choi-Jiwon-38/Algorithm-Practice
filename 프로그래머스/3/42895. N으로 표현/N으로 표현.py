def solution(N, number):
    num_dict = dict()
    arr = [[] for _ in range(9)]

    if N == number:
        return 1
    
    arr[1].append(N)
    num_dict[N] = True
    
    for i in range(2, 9):
        arr[i].append(int(str(N) * i))
        num_dict[arr[i][0]] = True
        
        if arr[i][0] == number:
            return i
        
        for j in range(1, i):
            left = arr[j]
            right = arr[i - j]
            
            for k in range(len(left)):
                for l in range(len(right)):
                    if right[l] == 0:
                        continue
                    
                    for next_num in [left[k] + right[l], left[k] - right[l], left[k] * right[l], left[k] // right[l]]:
                        if next_num > 0 and next_num not in num_dict:
                            num_dict[next_num] = True
                            arr[i].append(next_num)
                            
                            if next_num == number:
                                return i
            
    return -1