import sys
from itertools import combinations

while True :
    num_list = list(map(int, sys.stdin.readline().split()))

    if num_list[0] == 0 :
        break

    num_types = list(combinations(num_list[1:], 6))
    for i in range(len(num_types)) :
        tmp = list(num_types[i])
        tmp.sort()
        num_types[i] = tmp
    
    for n in num_types :
        for ele in n :
            print(ele, end=' ')
        print()
    print()
