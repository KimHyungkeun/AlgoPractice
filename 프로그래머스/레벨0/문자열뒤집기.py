def solution(my_string):
    my_string = list(my_string)
    ans_list = list(reversed(my_string))
    answer = ''.join(ans_list)
    return answer