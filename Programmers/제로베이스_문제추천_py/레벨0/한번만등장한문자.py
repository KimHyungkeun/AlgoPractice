def solution(s):
    answer = ''
    key_dict = {}
    list_s = sorted(list(s))
    
    for key in list_s :
        if key not in key_dict :
            key_dict[key] = 1
        else :
            key_dict[key] += 1
    
    for key in key_dict.keys() :
        if key_dict[key] == 1 :
            answer += key
    
    return answer