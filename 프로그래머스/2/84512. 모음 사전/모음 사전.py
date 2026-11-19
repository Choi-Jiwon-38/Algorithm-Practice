def make_all_word(words, curr = '', step = 1):
    for a in ['A', 'E', 'I', 'O', 'U']:
        words.append(curr + a)
        
        if step == 5:
            continue
        
        make_all_word(words, curr + a, step + 1)

    

def solution(word):    
    answer = 0
    words = []
    
    make_all_word(words)
    
    for i in range(len(words)):
        if words[i] == word:
            return i + 1