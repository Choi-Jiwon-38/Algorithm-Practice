let maxCount = 0;

function go_dungeon(visited, dungeons, k, count) {
    maxCount = Math.max(maxCount, count);
    
    for (let i = 0; i < dungeons.length; i++) {        
        if (!visited[i]) {
            if (k >= dungeons[i][0]) {
                visited[i] = true;
                go_dungeon(
                    visited,
                    dungeons,
                    k - dungeons[i][1],
                    count + 1
                );
                visited[i] = false;   
            }
        }
    }
}

function solution(k, dungeons) {
    maxCount = 0;
    
    const visited = Array(dungeons.length).fill(false);
    
    go_dungeon(visited, dungeons, k, 0);
    
    return maxCount;
}