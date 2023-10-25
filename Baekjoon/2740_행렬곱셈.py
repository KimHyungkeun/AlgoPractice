import sys

matrix1 = []
matrix2 = [] 
result_matrix = []

n, m = map(int, sys.stdin.readline().split())
for _ in range(n) :
    arr = list(map(int, sys.stdin.readline().split()))
    matrix1.append(arr)

m, k = map(int, sys.stdin.readline().split())
for _ in range(m) :
    arr = list(map(int, sys.stdin.readline().split()))
    matrix2.append(arr)

for mat1 in matrix1 :
    
    tmp_arr = []
    for j in range(k) :
        tmp = 0
        for t in range(m) :
            tmp += (mat1[t] * matrix2[t][j])
        tmp_arr.append(tmp)
    result_matrix.append(tmp_arr)


for r in result_matrix :
    for val in r :
        print(val, end=' ')
    print()
