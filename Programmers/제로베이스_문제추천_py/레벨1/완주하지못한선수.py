def solution(participant, completion):
    answer = ''
    com_dict = {}
    
    for p in participant :
        if p not in com_dict :
            com_dict[p] = 1
        else :
            com_dict[p] += 1
    
    for c in completion :
        com_dict[c] -= 1
    
    for p in participant :
        if com_dict[p] != 0 :
            answer = p
            break
            
    return answer