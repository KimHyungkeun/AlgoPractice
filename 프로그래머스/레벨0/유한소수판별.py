def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def solution(a, b):
    answer = 0
    val = gcd(a, b)

    b //= val
    
    soinsu = set([])
    sosu = 2
    
    while b != 1 :
        if b % sosu == 0 :
            b //= sosu
            soinsu.add(sosu)
        else :
            sosu += 1
    
    if 2 in soinsu :
        soinsu.remove(2)
    if 5 in soinsu :
        soinsu.remove(5)
    
    if len(soinsu) == 0 :
        answer = 1
    else : 
        answer = 2
        
    return answer

print(solution(7, 20))