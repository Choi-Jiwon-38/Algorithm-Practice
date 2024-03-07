function solution(n, words) {
    var answer = [0, 0];
    
    let map = new Map();    
    let lastWord = words[0][0];
    let count = 1;
    
    for (let word of words) {
        if (lastWord !== word[0]) { // 시작하는 단어를 틀린 경우
            (count % n == 0)
                ?   // n번째 사람인 경우
                    answer = [n, parseInt(count / n)]
                : 
                    answer = [count % n, parseInt(count / n) + 1];
            
            return answer;
        }
        
        let value = map.get(word);
        
        if (value === true) { // 이미 나온 단어를 말한 경우
            (count % n == 0)
                ?   // n번째 사람인 경우
                    answer = [n, parseInt(count / n)]
                : 
                    answer = [count % n, parseInt(count / n) + 1];
            
            return answer;
        }
        
        lastWord = word[word.length - 1];
        map.set(word, true);
        count++;
    }

    return answer;
}