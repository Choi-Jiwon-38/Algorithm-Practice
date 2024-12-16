import itertools

def solution(clothes):
    dic = {}
    
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        if not key in dic:
            dic[key] = []
        
        dic[key].append(value)
        
        
    print(dic)
        
    value_list = list(dic.values())

    
    a = itertools.product(*value_list)

    

    return len(list((a)))