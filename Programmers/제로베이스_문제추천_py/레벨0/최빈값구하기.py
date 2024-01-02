def solution(array):
    key_dict = {}
    answer = 0
    
    for a in array :
        if a not in key_dict :
            key_dict[a] = 1
        else :
            key_dict[a] += 1
    
    items = sorted(key_dict.items(), key = lambda x : x[1], reverse=True)
    max_val = items[0][1]
    
    cnt = 0
    for idx in range(len(items)) :
        if items[idx][1] == max_val :
            cnt += 1
        if cnt == 2 :
            break
    
    if cnt == 2 :
        answer = -1
    else :
        answer = items[0][0]
        
    return answer