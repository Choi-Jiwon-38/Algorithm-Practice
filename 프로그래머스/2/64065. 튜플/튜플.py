def solution(s):
    answer = []
    
    s = s[2:-2]
    group = s.split("},{")
    
    nums = [sorted(list(map(int, g.split(",")))) for g in group]
    nums.sort(key=lambda x: len(x))
    
    # base case
    answer.append(nums[0][0])
    
    # recursive case
    for i in range(1, len(nums)):
        flag = False
        
        for j in range(len(nums[i - 1])):
            if nums[i][j] != nums[i - 1][j]:
                answer.append(nums[i][j])
                flag = True
                break
        
        if not flag:
            answer.append(nums[i][-1])
    

    return answer