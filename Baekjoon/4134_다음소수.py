# 230703 retry success
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    n = int(sys.stdin.readline().rstrip())

    while True :
        sqrt = n ** 0.5

        if sqrt == int(sqrt) :
            n += 1
            continue

        flag = True
        for i in range(2, int(sqrt)+1) :
            if n % i == 0 :
                flag = False
                break
        if flag :
            break

        n += 1
    
    print(n)



# 테스트 케이스 (230702)
# t = int(sys.stdin.readline().rstrip())

# for _ in range(t) :
#     n = int(sys.stdin.readline().rstrip())

#     while True :
#         sqrt = n ** 0.5

#         # 거듭제곱근이면 합성수이므로 다음 수로 넘어감
#         if sqrt == int(sqrt) :
#             n += 1
#             continue
        
#         # n 이외의 수로 나누어떨어지지 않으면 소수
#         flag = True
#         for i in range(2, int(sqrt)+1) :
#             if n % i == 0 :
#                 flag = False
#                 break
        
#         if flag :
#             break

#         n += 1
    
#     print(n)