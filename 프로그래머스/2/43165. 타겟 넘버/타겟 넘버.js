let answer = 0;

function make_list(numbers, target, step) {
    if (numbers.length === step) {
        if (numbers.reduce((acc, cur) => acc + cur, 0) === target) {
            answer++;
        }
    } else {    
        make_list(numbers, target, step + 1);
        numbers[step] *= -1;
        make_list(numbers, target, step + 1)
    }
}


function solution(numbers, target) {
    make_list(numbers, target, 0)
    
    return answer;
}