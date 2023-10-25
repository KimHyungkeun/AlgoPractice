import sys

n, d = map(int, sys.stdin.readline().split())
cnt = 0
arr = []
for i in range(n) :
    arr.append(i+1)

for a in arr :
    list_num = str(a)
    cnt += list_num.count(str(d))

print(cnt)
