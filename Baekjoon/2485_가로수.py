from collections import deque
from math import gcd
import sys

n = int(sys.stdin.readline().rstrip())
num_list = []
distance = []

# 가로수 리스트
for _ in range(n) :
    num_list.append(int(sys.stdin.readline().rstrip()))

# 가로수 별 간격 리스트
for i in range(len(num_list)-1) :
    distance.append(abs(num_list[i] - num_list[i+1]))

# 간격 리스트 내에서 최대공약수를 구함
result = 0   
for i in range(len(num_list)-1) :
    if i == 0 :
        result = gcd(distance[i], distance[i+1])
    else :
        result = gcd(result, distance[i])

# 간격 별 지어야 할 가로수 갯수는, 간격을 최대공약수로 갯수에서 1을 뺀 값
cnt = 0
for d in distance :
    cnt += ((d // result) - 1)

print(cnt)
