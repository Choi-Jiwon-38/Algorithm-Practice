function solution(s) {
    let wordList = s.split(" ");
    let answer = '';
    
    for (let i = 0; i < wordList.length; i++) {
        let word = wordList[i];
        for (let j = 0; j < word.length; j++) {
            (j % 2 === 0)
                ? answer += word[j].toUpperCase()
                : answer += word[j].toLowerCase();
        }
        if (i < wordList.length - 1)
            answer += " ";
        
    }
    
    return answer;
}