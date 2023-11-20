def solution(genres, plays):
    answer = []
    tracks = {}
    tracks_play_sum = {}
    
    for i in range(len(genres)) :
        if genres[i] not in tracks :
            tracks[genres[i]] = [(plays[i], i)]
        else :
            tracks[genres[i]].append((plays[i], i))
        
        if genres[i] not in tracks_play_sum :
            tracks_play_sum[genres[i]] = plays[i]
        else :
            tracks_play_sum[genres[i]] += plays[i]
    
    for key in tracks.keys() :
        tracks[key].sort(key = lambda x : x[1])
        tracks[key].sort(key = lambda x : x[0], reverse=True)
    
    tracks_sort_by_num = sorted(tracks_play_sum.items(), key = lambda x : x[1], reverse=True)
    

    for t in tracks_sort_by_num :
        tmp = []
        for val in tracks[t[0]] :
            tmp.append(val[1])
            if len(tmp) == 2 :
                break
        while tmp :
            answer.append(tmp.pop(0))
    return answer