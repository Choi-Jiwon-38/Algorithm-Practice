def solution(genres, plays):
    n = len(genres)
    answer = []
    
    genre_dict = dict()

    for i in range(n):
        if genres[i] in genre_dict:
            genre_dict[genres[i]].append([plays[i], i])
        else:
            genre_dict[genres[i]] = [[plays[i], i]]
        
    genre_key = list(genre_dict.keys())
    genre_key.sort(key=lambda x: -sum(y[0] for y in genre_dict[x]))
    
    print(genre_key)
    
    for key in genre_key:
        genre_dict[key].sort(key=lambda x: (-x[0], x[1]))
        
        for i in range(min(2, len(genre_dict[key]))):
            answer.append(genre_dict[key][i][1])
    
    return answer