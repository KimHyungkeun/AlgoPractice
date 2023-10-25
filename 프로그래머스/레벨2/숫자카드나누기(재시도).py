
# 정답코드 https://school.programmers.co.kr/questions/44777
import math
def solution(arrayA,arrayB):
    gc,vc= 0,0

    for i in range(len(arrayA)):
        gc = math.gcd(gc,arrayA[i])

    for i in range(len(arrayB)):
        vc = math.gcd(vc,arrayB[i])

    for j in range(len(arrayA)):
        if arrayA[j] % vc == 0:
            vc = 1
        if arrayB[j] % gc == 0:
            gc = 1

    if gc == 1 and vc ==1:
        return 0
    else:
        return max(gc,vc)
    
# 230409 오답
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(arrayA, arrayB):
    if len(arrayA) == 1 and len(arrayB) == 1 :
        return max(arrayA[0], arrayB[0])
    
    answer = 0
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    arrayA.sort()
    arrayB.sort()
    
    if len(arrayA) == 2 and len(arrayB) == 2 :
        a_flag = False
        b_flag = False
        a_gcd = gcd(arrayA[0], arrayA[1])
        b_gcd = gcd(arrayB[0], arrayB[1])
        
        for a in arrayA :
            if a % b_gcd == 0 :
                b_flag = True
                break
        
        for b in arrayB :
            if b % a_gcd == 0 :
                a_flag = True
                break
                
        if not a_flag and not b_flag :
            return max(a_gcd, b_gcd)
        elif a_flag :
            return b_gcd
        elif b_flag :
            return a_gcd
        else :
            return 0
    
    if len(arrayA) >= 3 and len(arrayB) >= 3 :
        a_flag = False
        b_flag = False
        a_gcd = gcd(arrayA[0], arrayA[1])
        b_gcd = gcd(arrayB[0], arrayB[1])
        
        for i in range(2, len(arrayA)) :
            a_gcd = gcd(a_gcd, arrayA[i])
        for i in range(2, len(arrayB)) :
            b_gcd = gcd(b_gcd, arrayB[i])
        
        for a in arrayA :
            if a % b_gcd == 0 :
                b_flag = True
                break
        
        for b in arrayB :
            if b % a_gcd == 0 :
                a_flag = True
                break
                
        if not a_flag and not b_flag :
            return max(a_gcd, b_gcd)
        elif a_flag :
            return b_gcd
        elif b_flag :
            return a_gcd
        else :
            return 0
        
    return answer

arrayA = [10, 17]
arrayB = [5, 20]
solution(arrayA, arrayB)