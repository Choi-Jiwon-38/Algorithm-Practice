function solution(numbers) {
    var answer = 45;
    for (let num of numbers) {
        answer -= num;
    }
    return answer;
}