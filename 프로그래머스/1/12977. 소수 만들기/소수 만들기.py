def solution(nums):
    answer = 0
    limit = 3001
    isPrime = [True for _ in range(limit)]
    isPrime[0] = isPrime[1] = 0
    
    for i in range(2, int(limit ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * 2, limit + 1, i):
                isPrime[j] = False
        
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if isPrime[nums[i] + nums[j] + nums[k]]:
                    answer += 1
        
        
    return answer