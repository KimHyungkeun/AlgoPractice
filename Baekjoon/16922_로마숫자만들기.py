import sys
from itertools import combinations_with_replacement
rome_dict = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50}
rome_type = ['I', 'V', 'X', 'L']

n = int(sys.stdin.readline().rstrip())
result = list(combinations_with_replacement(rome_type, n))

num_combi_list = set([])
for r in result :
    total = 0
    for i in range(n) :
        total += rome_dict[r[i]]
    num_combi_list.add(total)

print(len(num_combi_list))

