def solution(X, Y):
    answer = ''
    num_arr = []
    
    X_dict = {i:0 for i in range(0, 10)}
    Y_dict = {i:0 for i in range(0, 10)}
    
    for ele in X :
        X_dict[int(ele)] += 1
    
    for ele in Y :
        Y_dict[int(ele)] += 1
    
    for key in range(0, 10) :
        if X_dict[key] < Y_dict[key] :
            val = X_dict[key]
        else : 
            val = Y_dict[key]
        
        num_arr.append(str(key)*val) 
    

    num_arr.sort(reverse=True)
    answer = ''.join(num_arr)
    
    if not answer :
        answer = "-1"
    
    elif len(answer) >= 2 :
        for i in range(len(answer)) :
            if answer[i] != '0' :
                break
        answer = answer[i:]
        
    return answer