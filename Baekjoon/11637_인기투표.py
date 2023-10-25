import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    n = int(sys.stdin.readline().rstrip())
    num_list = []
    for _ in range(n) :
        num_list.append(int(sys.stdin.readline().rstrip()))
    max_num = max(num_list)
    
    if num_list.count(max_num) > 1 :
        print("no winner")
    
    else :
        idx = num_list.index(max_num)
        if max_num > (sum(num_list) // 2) :
            print("majority winner " + str(idx+1))
        else :
            print("minority winner " + str(idx+1))


