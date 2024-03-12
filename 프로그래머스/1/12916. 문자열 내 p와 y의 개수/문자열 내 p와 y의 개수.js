function solution(str){
    let numOfP = 0;
    let numOfY = 0;

    for (let s of str) {
        if (s === 'p' || s === 'P')
            numOfP++;
        
        if (s === 'y' || s === 'Y')
            numOfY++;
    }
    
    return (numOfP === numOfY);
}