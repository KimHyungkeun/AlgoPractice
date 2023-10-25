import sys

n = int(sys.stdin.readline().rstrip())

matrix_a = []
matrix_b = []
result = []

for _ in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    matrix_a.append(row)

for _ in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    matrix_b.append(row)

cnt = 0
for i in range(n) :
    for j in range(n) :
        tmp = []
        for k in range(n) :
            if matrix_a[i][k] == 1 and matrix_b[k][j] == 1 :
                tmp.append(1)
            else :
                tmp.append(0)
        if 1 in tmp :
            cnt += 1

print(cnt)



