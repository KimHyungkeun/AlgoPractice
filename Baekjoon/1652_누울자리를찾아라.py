# 230515 풀이
import sys

n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n) :
    tmp = list(sys.stdin.readline().rstrip())
    board.append(tmp)

# 가로로 누울 자리
row_cnt = 0
for i in range(n) :
    cnt = 0
    for j in range(n) :
        if board[i][j] == '.' :
            cnt += 1
        else :
            if cnt >= 2 :
                row_cnt += 1
                cnt = 0
            else :
                cnt = 0
    if cnt >= 2 :
        row_cnt += 1

# 세로로 누울 자리
col_cnt = 0
for i in range(n) :
    cnt = 0
    for j in range(n) :
        if board[j][i] == '.' :
            cnt += 1
        else :
            if cnt >= 2 :
                col_cnt += 1
                cnt = 0
            else :
                cnt = 0
    if cnt >= 2 :
        col_cnt += 1

print(row_cnt, col_cnt)

# 이전 풀이(힌트 봤었음)
# import sys

# n = int(sys.stdin.readline())

# board = []
# for _ in range(n) :
#     arr = list(sys.stdin.readline())
#     board.append(arr)

# # 가로 누울 수 있는 공간 갯수
# row_cnt = 0
# for row in board :
#     cnt = 0
#     for space in row :
#         if space == '.' :
#             cnt += 1
#         else :
#             if cnt >= 2 :
#                 row_cnt += 1
#             cnt = 0
#     if cnt >= 2 :
#         row_cnt += 1
# # 세로로 누울 수 있는 공간 갯수
# col_cnt = 0
# for i in range(n) :
#     cnt = 0
#     for j in range(n) :
#         if board[j][i] == '.' :
#             cnt += 1
#         else :
#             if cnt >= 2 :
#                 col_cnt += 1
#             cnt = 0
#     if cnt >= 2 :
#         col_cnt += 1
        
# print(row_cnt, col_cnt)
