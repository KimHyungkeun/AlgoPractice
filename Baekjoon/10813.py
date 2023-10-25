import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for idx in range(n) :
    arr.append(idx+1)

for _ in range(m) :
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

for a in arr :
    print(a, end=' ')
