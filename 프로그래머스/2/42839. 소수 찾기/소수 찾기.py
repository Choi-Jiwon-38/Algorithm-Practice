def solution(numbers):
    answer = 0
    num_list = list(numbers)
    can_use = [True for _ in range(len(numbers))]
    
    all_num = set()
    
    
    def make_all_num(str_num, can_use, max_size):
        if len(str_num):
            all_num.add(int(str_num))
        
        if len(str_num) == max_size:
            return
        
        for i in range(len(can_use)):
            if can_use[i] == True:
                can_use[i] = False
                make_all_num(str_num + num_list[i], can_use, max_size)
                can_use[i] = True
    
    make_all_num('', can_use, len(numbers))
    max_num = max(all_num)
    
    print(max_num)
    
    isPrime = [True for _ in range(max_num + 1)]

    # base case
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, max_num + 1):
        if not isPrime[i]:
            continue
        
        for j in range(2, max_num // 2 + 1):
            if i * j <= max_num:
                isPrime[i * j] = False
            else:
                break
    
    for n in all_num:
        if isPrime[n]:
            answer += 1
    
    return answer