function solution(players, callings) {
    let playerMap = new Map();
    
    for (let i = 0; i < players.length; i++) {
        playerMap.set(players[i], i);
    }
    
    for (let call of callings) {
        // map을 idx를 찾는 용도로 사용
        let idx = playerMap.get(call);
        
        // swap
        let tmp = players[idx - 1];
        players[idx - 1] = call;
        players[idx] = tmp;
        
        // 바뀐 등수를 playerMap에도 반영
        playerMap.set(call, idx - 1);
        playerMap.set(tmp, idx);
    }
    return players;
}