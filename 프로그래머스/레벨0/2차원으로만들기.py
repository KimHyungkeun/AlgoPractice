def solution(num_list, n):
    answer = []
    
    tmp = []
    for num in num_list :
        if not tmp :
            tmp.append(num)
        else :
            if len(tmp) == n :
                answer.append(tmp)
                tmp = [num]
            else :
                tmp.append(num)
    
    answer.append(tmp)
    return answer