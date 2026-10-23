function solution(s){
    const stack = [];
    
    const match = {
        '(' : ')',
        ')' : null
    }
    
    for (const c of s) {
        if (stack.length) {
            if (match[stack[stack.length - 1]] === c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        } else { 
            if (match[c] === null) {
                return false
            }
            
            stack.push(c);
        }
    }
    
    return stack.length === 0
}