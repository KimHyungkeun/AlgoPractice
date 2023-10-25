import sys

n = int(sys.stdin.readline().rstrip())
num_dict = {}

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

for i in range(1, n) :
    if num_list[i-1] == num_list[i] :
        print(num_list[i])
        break