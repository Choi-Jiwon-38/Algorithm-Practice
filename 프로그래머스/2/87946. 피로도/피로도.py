answer = 0

def go_to_dungeon(k, visited, dungeons):
    global answer

    answer = max(visited.count(True), answer)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            go_to_dungeon(k - dungeons[i][1], visited, dungeons)
            visited[i] = False


def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))] 
    go_to_dungeon(k, visited, dungeons)

    return answer