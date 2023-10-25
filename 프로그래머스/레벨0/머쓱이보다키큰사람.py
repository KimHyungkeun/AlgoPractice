def solution(array, height):
    answer = 0
    array.sort(reverse=True)
    
    while array :
        if array[-1] <= height :
            array.pop()
        else : 
            break
    
    answer = len(array)
    return answer