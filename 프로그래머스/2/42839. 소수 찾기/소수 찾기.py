def make_nums(n, curr, str_nums, used, num_set, step = 0):
    if step == n:
        return
        
    for i in range(n):
        if not used[i]:
            used[i] = True
            make_nums(n, curr + str_nums[i], str_nums, used, num_set, step + 1)
            num_set.add(int(curr + str_nums[i]))
            used[i] = False
            
def prime_counter(nums):
    max_num = max(nums)
    is_prime = [True for _ in range(max_num + 1)]
    is_prime[0] = False
    is_prime[1] = False
    
    for num in range(2, int(max_num ** 0.5)):
        if not is_prime[num]:
            continue
    
        is_prime[num] = True
        
        for remove in range(num * 2, max_num + 1, num):
            is_prime[remove] = False
    
    count = 0
    
    for num in nums:
        if is_prime[num]:
            count += 1
    
    return count 
    
            
def solution(numbers):
    n = len(numbers)
    
    str_nums = list(numbers)
    used = [False for _ in range(n)]
    num_set = set()
    
    make_nums(n, '', str_nums, used, num_set)

    answer = prime_counter(num_set)

    return answer