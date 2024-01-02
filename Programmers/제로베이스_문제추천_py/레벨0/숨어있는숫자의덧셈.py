def solution(my_string):
    answer = 0
    num_arr = []
    tmp = ""
    for s in my_string :
        if '0' <= s <= '9' :
            tmp += s
        else :
            if tmp :
                num_arr.append(int(tmp))
                tmp = ""
    if tmp :
        num_arr.append(int(tmp))
    
    answer = sum(num_arr)
    return answer