def solution(my_string):
    answer = 0
    my_string = my_string.split()
    is_plus = False
    for i in range(len(my_string)) :
        if i == 0 :
            answer = int(my_string[i])
        else :
            if my_string[i] == '+' :
                is_plus = True
            elif my_string[i] == '-' :
                is_plus = False
            else :
                if is_plus :
                    answer += int(my_string[i])
                else :
                    answer -= int(my_string[i])
    return answer