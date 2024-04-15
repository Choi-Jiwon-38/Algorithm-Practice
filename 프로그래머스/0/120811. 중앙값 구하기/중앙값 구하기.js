function solution(array) {
    array.sort((a, b) => b - a);
    
    return array[parseInt(array.length / 2)];
}