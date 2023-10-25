# 230820 재풀이
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
c = list(map(int, sys.stdin.readline().split()))

ans = []
q = deque([])
for i in range(n) :
    if a[i] == 0 :
        q.append(b[i])

for num in c :
    q.appendleft(num)
    ans.append(q.pop())

for ele in ans :
    print(ele, end = ' ')


# import sys
# from collections import deque

# # stack = 0, queue = 1
# # 즉 stack은 LIFO구조라 맨 오른쪽에서 pop 되고
# # queue는 FIFO구조라서 맨 왼쪽에서 pop 된다
# # 이 때, c 수열에 해댱하는 값들을 차레대로 넣을 때, stack에 해당하는 자료구조는 사실상 변화가 없고, queue에 해당하는 자료구조 내부 원소만 바뀌므로
# # queue에 해당하는 자료구조 수열 끼리만 모은다.

# # queue에 해당하는 자료구조 수열 끼리만 모아서 또하나의 큐를 만든 후, 
# # appendleft를 통해 새로 들어오는 원소가 있으면 반대로 pop을 통해 빠져나가는 원소가 있을텐데 이 원소들을 모아 나열하여 출력한다
# ans = []
# n = int(sys.stdin.readline().rstrip())
# a = list(map(int, sys.stdin.readline().split()))
# b = list(map(int, sys.stdin.readline().split()))

# q = deque([])
# for i in range(len(b)) :
#     if a[i] == 0 :
#         q.append(b[i])

# m = int(sys.stdin.readline().rstrip())
# c = list(map(int, sys.stdin.readline().split()))

# for num in c :
#     q.appendleft(num)
#     ans.append(q.pop())

# for ele in ans :
#     print(ele, end = ' ')



