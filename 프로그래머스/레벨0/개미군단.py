def solution(hp):
    answer = 0
    
    if hp % 5 != 0 : 
        answer += (hp // 5)
        hp %= 5
    else :
        answer += (hp // 5)
        return answer
    
    if hp % 3 != 0 :
        answer += (hp // 3)
        hp %= 3
    else :
        answer += (hp // 3)
        return answer
    
    if hp % 1 != 0 :
        answer += (hp // 1)
        hp %= 1
    else :
        answer += (hp // 1)
        return answer
        
    