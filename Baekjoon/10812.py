from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n) :
    arr.append(i+1)

for _ in range(m) :
    i,j,k = map(int, sys.stdin.readline().split())
    begin = arr[0:i-1]
    mid = arr[i-1:j]
    end = arr[j:]

    val = arr[k-1]
    q = deque(mid)
    while q[0] != val :
        q.append(q.popleft())
    begin.extend(list(q))
    begin.extend(end)
    arr = begin

for a in arr :
    print(a, end=' ')
    

