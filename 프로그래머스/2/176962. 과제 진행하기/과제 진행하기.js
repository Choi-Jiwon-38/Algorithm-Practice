function timeToMinutes(time) {
    const [h, m] = time.split(":").map((x) => Number(x));
    return h * 60 + m;
}

function solution(plans) {
    plans.sort((a, b) => timeToMinutes(a[1]) - timeToMinutes(b[1]));
    const stopped = [];
    const answer = [];

    for (let i = 0; i < plans.length - 1; i++) {
        const [name, start, playtime] = plans[i];
        const nextStart = plans[i + 1][1];
        const availableTime = timeToMinutes(nextStart) - timeToMinutes(start);
        
        if (Number(playtime) > availableTime) { // 현재 진행 중인 과제를 못 끝내는 경우 
            stopped.push([name, Number(playtime) - availableTime])
        } else {
            answer.push(name);
            let restTime = availableTime - Number(playtime);
            
            while (restTime && stopped.length) {
                const [name, time] = stopped.pop();
                
                if (restTime >= time) {
                    answer.push(name);
                    restTime -= time;
                } else {
                    stopped.push([name, time - restTime]);
                    restTime = 0;  
                }
            }
        }
    }
    
    answer.push(plans[plans.length - 1][0]);
    
    while (stopped.length) {
        const [name] = stopped.pop();
        answer.push(name);
    }

    return answer;
}