import sys
def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
            
# 출처 : https://velog.io/@jieuihong/%EB%B0%B1%EC%A4%80-9020-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1%EC%8B%A4%EB%B2%841-Python