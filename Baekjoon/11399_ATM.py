import sys

n = int(sys.stdin.readline().rstrip())

num_list = list(map(int, sys.stdin.readline().split()))
num_accum_list = []

summary = 0
num_list.sort()

for i in range(len(num_list)) :
    summary += num_list[i]
    num_accum_list.append(summary)

print(sum(num_accum_list))