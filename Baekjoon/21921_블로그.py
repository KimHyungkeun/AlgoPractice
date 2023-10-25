import sys 
from collections import deque

n, x = map(int, sys.stdin.readline().split())
visit_num = list(map(int, sys.stdin.readline().split()))
visit_list = []

start = 0
end = x

total = sum(visit_num[start:end])
visit_list.append(total)
while end != n :
    total += visit_num[end]
    total -= visit_num[start]
    end += 1
    start += 1
    visit_list.append(total)

if max(visit_list) == 0 :
    print("SAD")
else :
    max_day = max(visit_list)
    max_cnt = visit_list.count(max_day)
    print(max_day)
    print(max_cnt)




