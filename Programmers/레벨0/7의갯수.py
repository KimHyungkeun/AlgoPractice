def solution(array):
    answer = 0
    
    num_str = ""
    cnt = 0
    for a in array :
        num_str += str(a)
    
    answer = num_str.count('7')
    return answer