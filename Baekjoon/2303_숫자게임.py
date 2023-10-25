import sys
from itertools import combinations

n = int(sys.stdin.readline())
people_tuple = []

for i in range(n) :
    people = list(map(int, sys.stdin.readline().split()))
    all_case = list(combinations(people, 3))

    sum_case = []
    for a in all_case :
        sum_case.append(int(str(sum(a))[-1]))
    

    people_tuple.append((i+1, max(sum_case))) 

people_tuple.sort(key = lambda x : x[1], reverse=True)
max_val = people_tuple[0][1]
winner = []

for p in people_tuple :
    if p[1] == max_val :
        winner.append(p[0])
    else :
        break

print(max(winner))