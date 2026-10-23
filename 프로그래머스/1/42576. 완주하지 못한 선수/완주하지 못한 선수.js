function solution(participant, completion) {
    var answer = '';
    
    p_set = {}
    c_set = {}
    
    for (const p of participant) {
        if (p in p_set) {
            p_set[p] += 1
        } else {
            p_set[p] = 1
        }
    }

    for (const c of completion) {
        if (c in c_set) {
            c_set[c] += 1
        } else {
            c_set[c] = 1
        }
    }
    
    for (const key of Object.keys(p_set)) {
        if (!(key in c_set)) { 
            // 참여자 명단에는 있지만 완주자 명단에는 없는 경우
            return key
        }
        
        if (p_set[key] > c_set[key]) {
            // 동명이인이 있어서 참여자 명단과 완주자 명단 수와 미일치한 경우
            return key
        }
    }
}