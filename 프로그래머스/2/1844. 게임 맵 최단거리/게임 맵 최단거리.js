function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    let flag = false;
    
    const queue = [[0, 0, 1]];
    let head = 0;
    
    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ];
    
    maps[0][0] = -2;
    
    while (queue.length > head) {
        const [cy, cx, cc] = queue[head];
        head++;
        
        for ([dy, dx] of dirs) {
            ny = cy + dy;
            nx = cx + dx;
            nc = cc + 1;
            
            if (ny >= 0 && nx >= 0 && ny < n && nx < m && maps[ny][nx] == 1) {
                maps[ny][nx] = -2;
                queue.push([ny, nx, nc]);
                
                
                if (ny == n - 1 && nx == m - 1) {
                    return cc + 1;
                }
            }
        }
    }
    
    return -1;
}