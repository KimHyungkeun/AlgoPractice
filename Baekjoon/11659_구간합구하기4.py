import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split())) 
accum_list = [] 

# 숫자 리스트에 대해 누적합을 저장한 누적합 리스트를 생성
sum = 0
for idx in range(len(num_list)) :
    sum += num_list[idx]
    accum_list.append(sum)

for _ in range(m) :
    i, j = map(int, sys.stdin.readline().split())
    if i == 1 :
        print(accum_list[j-1])
    else :
        print(accum_list[j-1] - accum_list[i-2])
