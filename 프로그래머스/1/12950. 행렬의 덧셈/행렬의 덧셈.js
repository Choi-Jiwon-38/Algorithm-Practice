function solution(arr1, arr2) {
    var answer = [];
    
    let rowLength = arr1.length;
    let colLength = arr1[0].length;
    
    for (let i = 0; i < rowLength; i++) {
        let tmp = [];
        for (let j = 0; j < colLength; j++) {
            tmp[j] = arr1[i][j] + arr2[i][j];
        }
        answer[i] = tmp;
    }
    
    return answer;
}