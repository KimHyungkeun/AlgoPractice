# import sys
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

# prime_arr = is_prime_number(1000000)

# while True :
#     n = int(sys.stdin.readline().rstrip())
#     if n == 0 :
#         break


# 답 : https://young1403.tistory.com/17
import sys
import math

arr = [True for i in range(1000001)]
primelist = []

def prime_list(x):
    global primelist
    for i in range(2,int(math.sqrt(1000000))+1):
        if arr[i] == True:
            for j in range(i+i,1000001,i):
                arr[j] = False
    primelist = [i for i in range(2,1000001) if arr[i] == True]

prime_list(1000000)

while True:
    n = int(sys.stdin.readline().rstrip())
    if not n:
        break       
    for i in primelist:
        if arr[n-i] :
            print('%d = %d + %d' %(n,i,n-i))
            break