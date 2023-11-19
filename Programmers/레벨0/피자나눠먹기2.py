def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n):
    answer = 0
    total_piece = lcm(n, 6)
    
    answer = total_piece // 6
    return answer