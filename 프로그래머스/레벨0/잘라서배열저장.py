def solution(my_str, n):
    answer = []
    
    tmp = ""
    for i in range(len(my_str)) :
        tmp += my_str[i]
        if len(tmp) == n :
            answer.append(tmp)
            tmp = ""
     
    if tmp :
        answer.append(tmp)
    return answer