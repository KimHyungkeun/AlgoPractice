def factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result

def solution(n):
    answer = 1
    
    for i in range(10, 0, -1) :
        if factorial(i) <= n :          
            answer = i
            break
    return answer