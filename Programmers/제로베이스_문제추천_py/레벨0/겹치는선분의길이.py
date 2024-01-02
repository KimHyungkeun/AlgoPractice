def solution(lines):
    answer = 0
    min_p = 101
    max_p = -101
    key_dict = {}
    
    for l in lines :
        if l[0] < min_p :
            min_p = l[0]
        if l[1] > max_p :
            max_p = l[1]
    
    for p in range(min_p, max_p) :
        key_dict[(p, p+1)] = 0
        
    for l in lines :
        for idx in range(l[0], l[1]) :
            key_dict[(idx,idx+1)] += 1
    
    cnt = 0
    for val in key_dict.values() :
        if val >= 2 :
            cnt += 1
    

    answer = cnt
    return answer