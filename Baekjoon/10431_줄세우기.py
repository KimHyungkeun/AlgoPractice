import sys

p = int(sys.stdin.readline().rstrip())

for _ in range(p) :
    num = list(map(int, sys.stdin.readline().split()))
    id = num[0]
    num_list = num[1:]
    cnt = 0
    
    for i in range(len(num_list)-1) :
        for j in range(i+1, len(num_list)) :
            if num_list[i] > num_list[j] :
                num_list[i], num_list[j] = num_list[j], num_list[i]
                cnt += 1
    
    print(id, cnt)