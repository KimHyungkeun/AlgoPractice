def solution(my_string, s, e):
    answer = ''
    reverse_string = ''.join(list(reversed(my_string[s:e+1])))
    answer = my_string[:s] + reverse_string + my_string[e+1:]
    return answer