answer = 51

def change(curr, target, words, used, step):
    global answer
    for i in range(len(words)):
        if used[i]:
            continue
        
        diff_count = 0
        word = words[i]
        
        for j in range(len(word)):        
            if curr[j] != word[j]:
                diff_count += 1
            
        if diff_count == 1:
            if target == word:
                answer = min(step + 1, answer)
            else:
                used[i] = True
                change(word, target, words, used, step + 1)
                used[i] = False
    

def solution(begin, target, words):
    # ealry return
    # target이 words 안에 없으면 변환 불가하므로 0 반환
    if not target in words:
        return 0

    used = [False for _ in range(len(words))]
    change(begin, target, words, used, 0)

    return answer