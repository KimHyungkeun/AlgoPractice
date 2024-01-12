def solution(n, lost, reserve):
    answer = 0
    
    result = []
    suits_dict = {i:1 for i in range(1, n+1)}
    for r in reserve :
        suits_dict[r] = 2
    for l in lost :
        suits_dict[l] -= 1
    
    for key,val in suits_dict.items() :
        result.append(val)
    
    for i in range(len(result)) :
        if result[i] == 0 :
            if i == 0 :
                if result[i+1] == 2 :
                    result[i] += 1
                    result[i+1] -= 1
            elif i == len(result)-1 :
                if result[i-1] == 2 :
                    result[i] += 1
                    result[i-1] -= 1
            else :
                if result[i-1] == 2 :
                    result[i] += 1
                    result[i-1] -= 1
                elif result[i+1] == 2 :
                    result[i] += 1
                    result[i+1] -= 1
                else :
                    None
                
                
    answer = len(result) - result.count(0)
    
    return answer