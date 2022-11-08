def solution(order):
    answer = 0
    string = str(order)
    
    for s in string :
        if s == '3' or s == '6' or s == '9' :
            answer += 1
    
    return answer