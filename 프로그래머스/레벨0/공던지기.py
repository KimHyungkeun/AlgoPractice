def solution(numbers, k):
    answer = 0
    length = len(numbers)
    
    i = -2
    for _ in range(k) :
        i = ((i+2) % length)
    
    answer = numbers[i]
    return answer