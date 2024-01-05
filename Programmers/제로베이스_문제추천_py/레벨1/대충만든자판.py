def solution(keymap, targets):
    answer = []
    key_dict = {}
    for i in range(len(keymap)) :
        for j in range(len(keymap[i])) :
            if keymap[i][j] not in key_dict :
                key_dict[keymap[i][j]] = [(i,j)]
            else :
                key_dict[keymap[i][j]].append((i,j))
    
    for word in key_dict.keys() :
        key_dict[word].sort(key = lambda x : x[1])
    
    for i in range(len(targets)) :
        total = 0
        for j in range(len(targets[i])) :
            if targets[i][j] not in key_dict :
                total = -1
                break
            else :
                total += (key_dict[targets[i][j]][0][1] + 1)
        
        answer.append(total)
        
    return answer