import sys

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

for n in num_list :
    print(n, end=' ')