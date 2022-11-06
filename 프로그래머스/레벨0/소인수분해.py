def solution(n):
    answer = []
    d = 2
    
    while n != 1 :
        if n % d == 0 :
            n //= d
            if d not in answer :
                answer.append(d)
        else :
            d += 1
    
    return answer