def solution(nums):
    dic = {}
    
    for num in nums:
        if (num in dic):
            dic[num] = dic[num] + 1 
        else:
            dic[num] = 0
    
    answer = min(len(dic), len(nums) // 2)
    return answer