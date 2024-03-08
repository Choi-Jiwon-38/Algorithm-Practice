function solution(dirs) {
    let x = 0;
    let y = 0;
    let set = new Set();
    
    for (let dir of dirs) {
        switch(dir) {
            case 'U':
                if (y === 5)
                    break;
                set.add(`(${x},${y})-(${x},${y+1})`);
                y++;
                break;
            case 'D':
                if (y === -5)
                    break;
                set.add(`(${x},${y-1})-(${x},${y})`);
                y--;
                break;
            case 'R':
                if (x === 5)
                    break;
                set.add(`(${x},${y})-(${x+1},${y})`);
                x++;
                break;
            case 'L':
                if (x === -5)
                    break;
                set.add(`(${x-1},${y})-(${x},${y})`);
                x--;
                break;
        }
    }
    
    return set.size;
}