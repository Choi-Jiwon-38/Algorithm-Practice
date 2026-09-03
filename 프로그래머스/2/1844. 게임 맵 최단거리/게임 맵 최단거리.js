function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const visited = Array.from({ length: n }, () => Array(m).fill(false));
    const q = [[0, 0, 1]];
    let head = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    
    visited[0][0] = true;
    
    while (head < q.length) {
        const [cy, cx, step] = q[head];
        head++;
        
        if (cy == n - 1 && cx == m - 1) {
            return step;
        }
        
        for (const dir of dirs) {
            const [dy, dx] = dir;
            const ny = cy + dy;
            const nx = cx + dx;
            
            if (ny >= 0 && ny < n && nx >= 0 && nx < m && !visited[ny][nx] && maps[ny][nx] !== 0) {
                visited[ny][nx] = true;
                q.push([ny, nx, step + 1])
            }
        }
    }
    
    return -1;
}