import sys

n,m = map(int, sys.stdin.readline().split())

arr_a = []
arr_b = []

for i in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    arr_a.append(tmp)

for i in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    arr_b.append(tmp)

for i in range(n) :
    for j in range(m) :
        print(arr_a[i][j] + arr_b[i][j], end=' ')
    print()

    