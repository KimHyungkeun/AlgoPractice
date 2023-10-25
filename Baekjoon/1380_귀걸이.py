import sys

cnt = 1
while True :
    n = int(sys.stdin.readline().rstrip())
    if n == 0 :
        break
    
    name_dict = {}
    called_dict = {}
    for i in range(n) :
        name = sys.stdin.readline().rstrip()
        name_dict[i+1] = name
        called_dict[i+1] = True
    
    for _ in range(2*n - 1) :
        num, alphabet = sys.stdin.readline().split()
        num = int(num)

        if called_dict[num] :
            called_dict[num] = False
        else :
            called_dict[num] = True
    
    for key in called_dict.keys() :
        if not called_dict[key] :
            break

    print(cnt, name_dict[key])
    cnt += 1 

