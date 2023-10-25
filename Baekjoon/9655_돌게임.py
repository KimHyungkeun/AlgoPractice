import sys

n = int(sys.stdin.readline())

# 돌은 3개 또는 1개 가져갈 수 있으므로, 일단 가장 먼저 최대한 많이 가져가야하는 3개씩을 가져간다
cnt = n % 3
n //= 3
cnt += n

if cnt % 2 != 0 :
    print("SK")
else :
    print("CY")
