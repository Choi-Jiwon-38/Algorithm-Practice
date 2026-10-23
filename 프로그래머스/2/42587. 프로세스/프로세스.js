function solution(priorities, location) {
    const p_stack = [...priorities].sort();
    max_p = p_stack[p_stack.length - 1]; 
    
    let count = 0;
    
    queue_head = 0;
    queue = [];
    
    for (let i in priorities) {
        queue.push([Number(i), priorities[i]]);
    }
    
    while (queue_head < queue.length) {
        task = queue[queue_head];
        queue_head++;
        
        if (task[1] < max_p) {
            queue.push(task);
        } else {
            p_stack.pop();
            max_p = p_stack[p_stack.length - 1];
            count++;
            if (task[0] === location) {
                break;
            }
        }
    }
    
    return count;
}