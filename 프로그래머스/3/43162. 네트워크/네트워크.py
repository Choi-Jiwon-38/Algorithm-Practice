def dfs(visit, computers, index, answer):
    if visit[index] == True:
        return;
    
    visit[index] = True
    
    for i in range(len(computers)):
        if computers[index][i] == 1:
            dfs(visit, computers, i, answer)
    

def solution(n, computers):
    answer = 0
    visit = [False for _ in range(len(computers))]

    for i in range(len(computers)):
        if visit[i] == False:
            answer += 1
            dfs(visit, computers, i, answer)

    return answer