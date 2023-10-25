# 정답 코드
def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = [] 

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divisors.append(i)
            if (i != (n // i)): 
                divisors_back.append(n//i)

    print("divisors : ", divisors)
    print("divisors_back : ", divisors_back)
    return divisors + divisors_back[::-1]

def solution(number, limit, power):
    answer = 0
    weapon_list = []
    
    for i in range(1, number+1) :
        cnt = len(get_divisor(i))
        weapon_list.append(cnt)
    
    for w in weapon_list :
        if w > limit :
            answer += power
        else :
            answer += w
    return answer
# 참고 : https://inuplace.tistory.com/459



solution(5, 3, 2)


# 20221206 시간초과
# import math
# # 소수 판별 함수(에라토스테네스의 체)
# def is_prime_number(n):
#     # 2부터 n까지의 모든 수에 대하여 소수 판별
#     array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

#     # 에라토스테네스의 체
#     for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
#         if array[i] == True: # i가 소수인 경우(남은 수인 경우)
#             # i를 제외한 i의 모든 배수를 지우기
#             j = 2
#             while i * j <= n:
#                 array[i * j] = False
#                 j += 1

#     return [ i for i in range(2, n+1) if array[i] ]   

# def solution(number, limit, power):
#     answer = 0
#     weapon_list = []
#     is_prime = is_prime_number(number)
    
#     for i in range(1, number+1) :
#         cnt = 0
#         if i == 1 :
#             weapon_list.append(1)
#         if i in is_prime :
#             weapon_list.append(2)
#         else :
#             weapon_list.append(cnt)
    
#     return answer


