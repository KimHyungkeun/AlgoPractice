import sys

n, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
accum_list = []

# 누적합 리스트 생성
total = 0
for num in num_list :
    total += num
    accum_list.append(total)

# 연속 k개의 누적합 리스트 중 가장 최대값을 선정
result = []
for i in range(k-1, n) :
    if i == k-1 :
        result.append(accum_list[i])
    else :
        result.append(accum_list[i] - accum_list[i-k])

print(max(result))
