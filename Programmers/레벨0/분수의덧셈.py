def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b): # 최소공배수
    return a * b // gcd(a, b)

def solution(denum1, num1, denum2, num2):
    answer = []
    bunmo = lcm(num1, num2); # 분모를 통분
    bunja1 = denum1 * (bunmo // num1)
    bunja2 = denum2 * (bunmo // num2)
    bunja = bunja1 + bunja2 # 통분한 분모를 기준으로 분자를 더함
    
    div = gcd(bunja, bunmo) # 분자, 분모간의 최대공약수를 구함
    
    answer = [bunja // div, bunmo // div] # 해당 분수를 기약분수로 변환
    return answer