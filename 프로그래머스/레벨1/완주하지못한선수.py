def solution(participant, completion):
    answer = ''
    part_key = {}
    for p in participant :
        if p in part_key : 
            part_key[p] += 1
        else :
            part_key[p] = 1
    
    for c in completion :
        part_key[c] -= 1
    
    for key in part_key.keys() :
        if part_key[key] == 1 :
            answer = key
            break
    return answer