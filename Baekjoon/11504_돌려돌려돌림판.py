# 230922 retry Success
import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    n, m = map(int, sys.stdin.readline().split())
    x = list(sys.stdin.readline().split())
    y = list(sys.stdin.readline().split())
    circle_board = list(sys.stdin.readline().split())
    circle_board += circle_board[:m]

    int_x = int(''.join(x))
    int_y = int(''.join(y))

    cnt = 0
    for i in range(n) :
        val = int(''.join(circle_board[i:i+m]))
        if int_x <= val <= int_y :
            cnt += 1
    
    print(cnt) 


# 230921 solved but searched answer
# import sys

# t = int(sys.stdin.readline().rstrip())
# for _ in range(t) :
#     n, m = map(int, sys.stdin.readline().split())
#     x = list(sys.stdin.readline().split())
#     y = list(sys.stdin.readline().split())
#     num_x = int(''.join(x))
#     num_y = int(''.join(y))
#     board = list(sys.stdin.readline().split())
#     board += board[:m]
    
#     cnt = 0
#     for i in range(n) :
#         if num_x <= int(''.join(board[i:i+m])) <= num_y :
#             cnt += 1
    
#     print(cnt)
    

# 1% 오답
# import sys

# t = int(sys.stdin.readline().rstrip())
# for _ in range(t) :
#     n, m = map(int, sys.stdin.readline().split())
#     x = list(map(int, sys.stdin.readline().split()))
#     y = list(map(int, sys.stdin.readline().split()))
#     board = list(map(int, sys.stdin.readline().split()))
#     board_case = []

#     for i in range(m) :
#         cnt = 0
#         for b in board :
#             if x[i] <= b <= y[i] : 
#                 cnt += 1
#         board_case.append(cnt)
            
#     print(min(board_case))