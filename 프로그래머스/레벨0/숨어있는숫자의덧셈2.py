def solution(my_string):
    answer = 0
    tmp = ""
    for s in my_string :
        if '0' <= s <= '9' :
            tmp += s
        else :
            if tmp :
                answer += int(tmp)
                tmp = ""
    if tmp :
        answer += int(tmp)
    return answer