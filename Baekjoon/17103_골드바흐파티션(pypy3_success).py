# 230703 pypy3 한정 성공
import sys
import math
from collections import deque

# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]   


t = int(sys.stdin.readline().rstrip())
prime_list = is_prime_number(1000000)
q = deque(prime_list)

prime_dict = {}
for i in range(2, 1000000) :
    if q and i == q[0] :
        prime_dict[q.popleft()] = True
    else :
        prime_dict[i] = False
  
for _ in range(t) :
    n = int(sys.stdin.readline().rstrip())
    half = n // 2

    cnt = 0
    for i in range(2, half+1) :
        left = i
        right = n - i

        # 이미 한번 찾은 소수는 이곳에서 확인
        if prime_dict[left] and prime_dict[right] :
            cnt += 1
    
    print(cnt)