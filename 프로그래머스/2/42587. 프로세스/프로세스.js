function solution(priorities, location) {
    const stack = [...priorities].sort();
    const p = priorities.map((x, i) => [x, i]);
    let count = 0
    
    while (true) {
        count++;
        
        while (stack[stack.length - 1] > p[0][0]) {
            const tmp = p[0]
            p.shift();
            p.push(tmp);
        }
    
        const tmp = p[0]
        p.shift();
        stack.pop();
    
        if (location == tmp[1]) {
            return count;
        }
    }
}