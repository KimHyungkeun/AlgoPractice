def solution(array):
    num_dict = {}
    for a in array :
        if a in num_dict :
            num_dict[a] += 1
        else :
            num_dict[a] = 1
    
    sorted_dict = sorted(num_dict.items(), key = lambda item: item[1], reverse = True)
    
    if (len(sorted_dict) == 1) :
        answer = sorted_dict[0][0]
    
    elif (sorted_dict[0][1] == sorted_dict[1][1]) :
        answer = -1
        
    else :
        answer = sorted_dict[0][0]
    
    return answer