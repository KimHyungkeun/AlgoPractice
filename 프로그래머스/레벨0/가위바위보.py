def solution(rsp):
    answer = ''
    
    for win in rsp :
        if win == "2" :
            answer += "0"
        elif win == "0" :
            answer += "5"
        else :
            answer += "2"
    return answer