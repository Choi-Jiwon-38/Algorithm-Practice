function solution(s) {
    let len = s.length;
    
    if (len !== 4 && len !== 6)
        return false;
    
    for (let c of s) {
        if (isNaN(+c)) 
            return false;
    }
    
    return true;
}