function solution(triangle) {
    for (let i = 1; i < triangle.length; i++) {
        let lineLen = triangle[i].length;
        for (let j = 0; j < lineLen; j++) {
            if (j === 0) { // 맨 좌측
                triangle[i][0] += triangle[i-1][0];
            } else if (j === lineLen - 1) { // 맨 우측
                triangle[i][lineLen - 1] += triangle[i-1][lineLen - 2]; 
            } else { // 나머지
                (triangle[i-1][j] > triangle[i-1][j-1])
                    ? triangle[i][j] += triangle[i-1][j]
                    : triangle[i][j] += triangle[i-1][j-1];
            }
        }
        
    }

    return Math.max(...triangle[triangle.length - 1]);
}