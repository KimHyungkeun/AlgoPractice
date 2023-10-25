# 230614 재시도 성공
import sys

n, m = map(int, sys.stdin.readline().split())

area_list = []

for _ in range(n) :
    area_list.append(list(map(int, sys.stdin.readline().split())))

cnt = 0

# 위, 아래
cnt += ((n*m) * 2)

# 앞
for i in range(m) :
    for j in range(n-1, -1 ,-1) :
        if j == n-1 :
            cnt += area_list[j][i]
        else :
            if area_list[j+1][i] <= area_list[j][i] :
                cnt += (area_list[j][i] - area_list[j+1][i])

# 뒤
for i in range(m) :
    for j in range(n) :
        if j == 0 :
            cnt += area_list[j][i]
        else :
            if area_list[j-1][i] <= area_list[j][i] :
                cnt += (area_list[j][i] - area_list[j-1][i])

# 좌
for i in range(n) :
    for j in range(m) :
        if j == 0 :
            cnt += area_list[i][j]
        else :
            if area_list[i][j-1] <= area_list[i][j] :
                cnt += (area_list[i][j] - area_list[i][j-1])

# 우
for i in range(n) :
    for j in range(m-1, -1, -1) :
        if j == m-1 :
            cnt += area_list[i][j]
        else :
            if area_list[i][j+1] <= area_list[i][j] :
                cnt += (area_list[i][j] - area_list[i][j+1])

print(cnt)

# 230519(힌트 봤음)
# 힌트 : https://dailylifeofdeveloper.tistory.com/175
# import sys

# n, m = map(int, sys.stdin.readline().split())
# board = []
# up_down_cnt = 0
# for _ in range(n) :
#     tmp = list(map(int, sys.stdin.readline().split()))
#     board.append(tmp)

# # 위, 아래에 대한 면적
# up_down_cnt += ((n*m) * 2)

# # 앞, 뒤에 대한 면적
# front_cnt = 0
# for i in range(m) :
#     cnt = 0
#     for j in range(n) :
#         if j == 0 :
#             cnt += board[j][i]
#         else :
#             if board[j][i] - board[j-1][i] > 0 :
#                 cnt += (board[j][i] - board[j-1][i])
#     front_cnt += cnt

# back_cnt = 0
# for i in range(m-1, -1 ,-1) :
#     cnt = 0
#     for j in range(n-1, -1, -1) :
#         if j == n-1 :
#             cnt += board[j][i]
#         else :
#             if board[j][i] - board[j+1][i] > 0 :
#                 cnt += (board[j][i] - board[j+1][i])
#     back_cnt += cnt

# # 왼, 오에 대한 면적
# left_cnt = 0
# for i in range(n) :
#     cnt = 0
#     for j in range(m) :
#         if j == 0 :
#             cnt += board[i][j]
#         else :
#             if board[i][j] - board[i][j-1] > 0 :
#                 cnt += (board[i][j] - board[i][j-1])    
#     left_cnt += cnt

# right_cnt = 0
# for i in range(n-1, -1, -1) :
#     cnt = 0
#     for j in range(m-1, -1 ,-1) :
#         if j == m-1 :
#             cnt += board[i][j]
#         else :
#             if board[i][j] - board[i][j+1] > 0 :
#                 cnt += (board[i][j] - board[i][j+1])    
#     right_cnt += cnt

# print(up_down_cnt + front_cnt + back_cnt + left_cnt + right_cnt)



# 오답
# import sys

# n, m = map(int, sys.stdin.readline().split())
# board = []
# cnt = 0
# for _ in range(n) :
#     tmp = list(map(int, sys.stdin.readline().split()))
#     board.append(tmp)

# # 위, 아래에 대한 면적
# cnt += ((n*m) * 2)

# # 4면에 대한 면적
# row_cnt = 0
# for i in range(n) :
#     row_cnt += (max(board[i]))
# row_cnt *= 2

# col_cnt = 0
# for i in range(m) :
#     max_num = -1
#     for j in range(n) :
#         if board[j][i] > max_num :
#             max_num = board[j][i]
#     col_cnt += max_num
# col_cnt *= 2

# # 보이지 않는 면에 대한 넓이
# unseen_cnt = 0
# for i in range(n) :
#     for j in range(1, m-1) :
#         if board[i][j-1] > board[i][j] :
#             unseen_cnt += (board[i][j-1] - board[i][j])
#         if board[i][j+1] > board[i][j] :
#             unseen_cnt += (board[i][j+1] - board[i][j])
# for i in range(m) :
#     for j in range(1, n-1) :
#         if board[j-1][i] > board[j][i] : 
#             unseen_cnt += (board[j-1][i] - board[j][i])
#         if board[j+1][i] > board[j][i] :
#             unseen_cnt += (board[j+1][i] - board[j][i])



# print(cnt + row_cnt + col_cnt + unseen_cnt)