from itertools import product
from functools import reduce
import sys

n = int(sys.stdin.readline().rstrip())
sakura_list = list(map(int, sys.stdin.readline().split()))

group_max_cnt = n - 3

num_list = [i for i in range(1, group_max_cnt+1)]
all_case = list(product(num_list, repeat=4))

result = []
for a in all_case :
    if sum(a) == n :
        result.append(a)

sum_list = []
for r in result :
    first = r[0]
    second = r[0] + r[1]
    third = r[0] + r[1] + r[2]
    last = r[0] + r[1] + r[2] + r[3]

    total = reduce(lambda x, y : x * y, sakura_list[:first]) + \
    reduce(lambda x, y : x * y, sakura_list[first:second]) + \
    reduce(lambda x, y : x * y, sakura_list[second:third]) + \
    reduce(lambda x, y : x * y, sakura_list[third:last])  
    sum_list.append(total)

print(max(sum_list))