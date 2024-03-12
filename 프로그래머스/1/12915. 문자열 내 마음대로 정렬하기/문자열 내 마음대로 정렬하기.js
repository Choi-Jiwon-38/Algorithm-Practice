function solution(strings, n) {
    var answer = strings;
    answer.sort(); // 먼저 사전순으로 정렬
    answer.sort(function (a, b) {
        // 각 문자열의 인덱스 n번째 글자를 기준으로 정렬
        if (a[n] < b[n]) { 
            return -1;
        }
        if (a[n] > b[n]) {
            return 1;
        }
        // n번째 글자가 같은 경우 -> 유지
        return 0;
    });
    
    return answer;
}