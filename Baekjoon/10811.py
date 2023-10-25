import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for idx in range(n) :
    arr.append(idx+1)

for _ in range(m) :
    i, j = map(int, sys.stdin.readline().split())
    first = arr[0:i-1]
    mid = list(reversed(arr[i-1:j]))
    last = arr[j:n]
    arr = first
    arr.extend(mid)
    arr.extend(last)

for a in arr :
    print(a, end=' ')
