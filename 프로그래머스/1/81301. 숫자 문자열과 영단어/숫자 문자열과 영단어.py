def solution(s):
    replace_map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    for word in replace_map.keys():
        s = s.replace(word, replace_map[word])
        
    return int(s)