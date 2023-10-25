def solution(s):
    answer = 0
    first_cnt = 0
    other_cnt = 0
    
    first_word = ""
    for w in s :   
        if first_cnt == 0 :
            first_word = w
            first_cnt += 1
        else :
            if w == first_word :
                first_cnt += 1
            else :
                other_cnt += 1
        
        if first_cnt == other_cnt :
            answer += 1
            first_cnt = 0
            other_cnt = 0
    
    if first_cnt + other_cnt >= 1 :
        answer += 1  
    return answer