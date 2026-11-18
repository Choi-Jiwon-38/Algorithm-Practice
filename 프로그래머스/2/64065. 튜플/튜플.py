def solution(s):
    tmp1 = list(s[1:-2].split('},'))
    
    tuples = []
    for tmp in tmp1:
        tuples.append(sorted(list(map(int, tmp[1:].split(",")))))
    
    tuples.sort(key=lambda x: len(x))
    
    answer = []
    
    count_dict = dict()
    count_dict[0] = []
    
    for i in range(len(tuples)):
        if i == 0:
            answer.append(tuples[i][0])
            continue
        
        flag = False
        
        for j in range(len(tuples[i - 1])):
            if tuples[i][j] != tuples[i - 1][j]:
                flag = True
                answer.append(tuples[i][j])
                break
        
        if not flag:
            answer.append(tuples[i][-1])
    
    return answer