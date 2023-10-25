def solution(babbling):
    answer = 0
    vibe = ["aya", "ye", "woo", "ma"]
    
    for b in babbling :
        tmp = ""
        for i in range(len(b)) :
            tmp += b[i]
            if tmp in vibe :
                tmp = ""
            if i == len(b)-1 :
                if tmp in vibe :
                    tmp = ""
        if not tmp :
            answer += 1
              
    return answer