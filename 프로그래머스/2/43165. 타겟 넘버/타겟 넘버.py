answer = {}

def dfs(numbers, target, depth = 1):
    global answer
    
    if sum(numbers) == target:
        answer[''.join(map(str, numbers))] = True
    
    if depth == len(numbers):
        return

    dfs(numbers, target, depth + 1)
    numbers[depth] *= -1
    dfs(numbers, target, depth + 1)
    

def solution(numbers, target):
    dfs(numbers, target)
    numbers[0] *= -1
    dfs(numbers, target)
    
    return len(answer)