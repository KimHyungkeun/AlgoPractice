import sys

num_list = []
N, M = map(int, sys.stdin.readline().split())
for i in range(N) :
    num_list.append(0)

for _ in range(M) :
    i,j,k = map(int, sys.stdin.readline().split())
    for t in range(i-1, j) :
        num_list[t] = k

for n in num_list : 
    print(n, end=' ')



