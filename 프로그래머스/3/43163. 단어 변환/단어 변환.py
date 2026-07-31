from collections import deque

def solution(begin, target, words):
    if not target in words:
        return 0
    
    answer = 0
    
    visited = [False for _ in range(len(words))]
    
    def dfs(visited, curr, count):
        nonlocal answer
        
        if curr == target:
            answer = count

        for i in range(len(words)):
            miss_count = 0
            word = words[i]
            
            for j in range(len(word)):
                if curr[j] != word[j]:
                    miss_count += 1
            
            # 변경할 수 있는 경우
            if miss_count == 1 and not visited[i]:
                visited[i] = True
                dfs(visited, word, count + 1)
                visited[i] = False
    
    dfs(visited, begin, 0)
                
    return answer