def solution(genres, plays):
    # classic: [0, []]
    # pop: [0, []]
    music = {}
    
    for i in range(len(genres)):
        if genres[i] in music:
            music[genres[i]][0] += plays[i]
            music[genres[i]][1].append([plays[i], i])
        else:
            music[genres[i]] = [plays[i], [[plays[i], i]]]
        
    print(music)
    
    sorted_genres = sorted(music.items(), key = lambda x: x[1][0], reverse=True)
    
    result = []
    
    for genre, (total_plays, songs) in sorted_genres:
        sorted_songs = sorted(songs, key=lambda x: (-x[0], x[1]))
        result.extend([song[1] for song in sorted_songs[:2]])
    
    return result
    