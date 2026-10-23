function solution(k, tangerine) {
    const t_map = new Map();
    
    for (const t of tangerine) {
        if (t_map.has(t)) {
            t_map.set(t, t_map.get(t) + 1);
        } else {
            t_map.set(t, 1);
        }
    }
    
    const valuesArray = [...t_map.values()].sort((a, b) => a - b);

    let remain = tangerine.length - k;
    
    count = 0;
    
    while (valuesArray[count] <= remain) {
        remain -= valuesArray[count];
        count++;
    }
    
    return valuesArray.length - count;
}