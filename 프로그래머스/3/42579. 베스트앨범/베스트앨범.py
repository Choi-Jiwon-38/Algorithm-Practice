def solution(genres, plays):
    musics = dict()
    n = len(plays)
    answer = []
    
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        
        if genre in musics:
            musics[genre].append([play, i])
        else:
            musics[genre] = [[play, i]]
        
    keys = list(musics.keys())
    
    keys.sort(key=lambda x: -sum(y[0] for y in musics[x])) 

    for key in keys:
        musics[key].sort(key=lambda x: (-x[0], x[1]))
        
        for i in range(min(2, len(musics[key]))):
            answer.append(musics[key][i][1])
    
    return answer