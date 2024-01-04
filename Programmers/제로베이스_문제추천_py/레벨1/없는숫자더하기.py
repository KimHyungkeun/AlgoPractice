def solution(numbers):
    answer = -1
    
    arr = [i for i in range(0,10)]
    set_result = set(arr) - set(numbers)
    result = list(set_result)
    
    answer = sum(result)
    return answer