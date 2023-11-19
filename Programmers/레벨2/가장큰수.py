def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x : str(x) * 3, reverse = True)
    
    for n in numbers :
        answer += str(n)
        
    answer = str(int(answer))
    return answer