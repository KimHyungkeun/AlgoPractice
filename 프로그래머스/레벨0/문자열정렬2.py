def solution(my_string):
    tmp = my_string.lower()
    string = list(tmp)
    string.sort()
    
    answer = ''.join(string)
    return answer