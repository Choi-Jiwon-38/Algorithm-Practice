function solution(x) {
    x = x.toString();
    
    let amount = 0;
    
    for (let i of x) {
        amount += +i;
    }
    
    return +x % amount === 0;
}