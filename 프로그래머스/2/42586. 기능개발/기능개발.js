function solution(progresses, speeds) {
    var answer = [];

    let curr_day;
    const stack = []
    
    for (let i = speeds.length - 1; i > -1; i--) {
        stack.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    
    let count;
    
    while (stack.length) {
        count = 0;
        curr_day = stack[stack.length - 1];
        
        console.log(curr_day);
        
        while (stack[stack.length - 1] <= curr_day) {
            stack.pop();
            count += 1
        }
        answer.push(count);
    } 
    
    return answer;
}