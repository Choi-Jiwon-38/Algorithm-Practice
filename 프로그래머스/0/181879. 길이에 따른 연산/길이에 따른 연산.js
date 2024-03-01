function solution(num_list) {
    var answer = 0;
    
    if (num_list.length < 11)
        answer = 1;
    
    for (let num of num_list) {
        num_list.length > 10 ? answer += num : answer *= num;
    }
    
    return answer;
}