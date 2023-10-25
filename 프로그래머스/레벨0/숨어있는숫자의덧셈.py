def solution(my_string):
    answer = 0
    
    for s in my_string :
        if "0" <= s <= "9" :
            answer += int(s)
    return answer