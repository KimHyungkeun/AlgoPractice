# 230925 Retry Success
import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    n = int(sys.stdin.readline().rstrip())
    candy_list = list(map(int, sys.stdin.readline().split()))
    
    q = deque(candy_list)
    cycle = 0

    while True :
        for i in range(len(q)) :
            if q[i] % 2 != 0 :
                q[i] += 1

        if len(set(q)) == 1 :
            break

        cycle += 1
        origin_q = deque([])
        move_right_q = deque([])

        for i in range(n) :
            origin_q.append(q[i] // 2)
            move_right_q.append(q[i] // 2)
        move_right_q.appendleft(move_right_q.pop())

        q = deque([])
        for i in range(n) :
            q.append(origin_q[i] + move_right_q[i])
    
    print(cycle)


# 230922 초기에 1%에서 오답. 풀긴 풀었으나 다시 재시도 도전
# import sys
# from collections import deque

# t = int(sys.stdin.readline().rstrip())
# for _ in range(t) :
#     n = int(sys.stdin.readline().rstrip())
#     candy_list = list(map(int, sys.stdin.readline().split()))

#     queue = deque(candy_list)
#     cycle = 0

#     while True :
#         for i in range(len(queue)) :
#             if queue[i] % 2 != 0 :
#                 queue[i] += 1
        
#         if len(set(queue)) == 1 :
#             break
        
#         cycle += 1
#         half_val_q = deque([])
#         move_right_q = deque([])
#         for q in queue :
#             half_val_q.append(q//2)
#             move_right_q.append(q//2)
#         move_right_q.appendleft(move_right_q.pop())

#         queue = deque([])
#         for i in range(n) :
#             queue.append(move_right_q[i] + half_val_q[i])
        
#         if len(set(queue)) == 1 :
#             break
        
#     print(cycle)

