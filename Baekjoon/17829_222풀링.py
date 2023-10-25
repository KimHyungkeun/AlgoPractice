import sys

n = int(sys.stdin.readline().rstrip())

total_list = []
for _ in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    total_list.append(row)

while len(total_list) != 1 :
    tmp_total_list = []

    for i in range(0, n, 2) :  
        tmp_row = []
        for j in range(0, n, 2) :
            tmp = [total_list[i][j], total_list[i][j+1], total_list[i+1][j], total_list[i+1][j+1]]
            tmp.sort()
            tmp_row.append(tmp[-2])
        tmp_total_list.append(tmp_row)


    total_list = tmp_total_list
    n //= 2

print(total_list[0][0])

    

