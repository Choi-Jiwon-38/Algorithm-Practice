function solution(num_list) {
    let odd = 0;
    let even = 0;
    
    for (let num of num_list)
        num % 2 === 0 ? even++ : odd++; 

    return [even, odd];
}