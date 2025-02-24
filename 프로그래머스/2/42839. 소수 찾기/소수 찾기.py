

def backtrack(nums, num_str, visited, prime_arr, answer_set, depth = 0):
    if prime_arr[int(num_str)]:
        answer_set.add(int(num_str))
  
    if depth == len(nums) - 1:
        return
    
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            backtrack(nums, num_str + nums[i], visited, prime_arr, answer_set, depth + 1)
            visited[i] = False 


def solution(numbers):
    max_num = int(''.join(sorted(list(numbers), reverse=True)))
    prime_arr = [False, False] + [True] * (max_num - 1)
    
    for i in range(2, max_num + 1):
        if prime_arr[i]:          
            for j in range(i * 2, max_num + 1, i):
                prime_arr[j] = False
    
    answer_set = set()
    visited = [False] * len(numbers)
    
    for i in range(len(numbers)):
        visited[i] = True
        backtrack(numbers, numbers[i], visited, prime_arr, answer_set)
        visited[i] = False
    
    return len(answer_set)