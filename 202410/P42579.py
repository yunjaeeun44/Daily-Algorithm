def solution(genres, plays):
    genresSet = {}
    for i in range(len(genres)):
        if genres[i] in genresSet:
            genresSet[genres[i]][0][0] += plays[i]
        else:
            genresSet[genres[i]] = [[plays[i], -1]]
        genresSet[genres[i]].append([plays[i], i])
    
    genresSong = sorted(list(genresSet.values()), key=lambda x: -x[0][0])
    
    answer = []
    for songs in genresSong:
        songs.sort(key = lambda x: (-x[0], x[1]))
        print(songs)
        for i in songs[1:3]:
            answer.append(i[-1])
        
    return answer