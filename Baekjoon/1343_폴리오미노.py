# 230517 재풀이 (성공)
import sys
poly_a = 'AAAA'
poly_b = 'BB'

poly_list = []
string = sys.stdin.readline().rstrip()

tmp = ""
for s in string :
    if s != '.' :
        tmp += s
    else :
        if tmp :
            poly_list.append(tmp)
        poly_list.append(s)
        tmp = ""

if tmp :
    poly_list.append(tmp)

flag = True
for i in range(len(poly_list)) :
    if poly_list[i] == '.' :
        continue

    flag = True
    tmp = ""
    len_p = len(poly_list[i])

    if len_p // len(poly_a) < 1 and len_p // len(poly_b) < 1: 
        flag = False
        break
    
    if len_p // len(poly_a) >= 1 :
        cnt = len_p // len(poly_a)
        tmp += (poly_a * cnt)
        len_p %= len(poly_a)

    if len_p // len(poly_b) >= 1 :
        cnt = len_p // len(poly_b)
        tmp += (poly_b * cnt)
        len_p %= len(poly_b)
    
    if len_p == 0 :
        poly_list[i] = tmp
    else :
        flag = False
        break
    
if not flag :
    print(-1)
else :
    print(''.join(poly_list))







# 반례게시판 찾아본 답
# import sys

# board_origin = sys.stdin.readline().rstrip()
# board = board_origin.split(".")
# only_x = []
# encoded_x = []
# poly_a = 'AAAA'
# poly_b = 'BB'

# # 'X'표시가 포함된 board만 따로 추출
# for b in board :
#     if b :
#         only_x.append(b)

# # 각 폴리오미노 별로, 완성된 폴리오미노 대입
# cannot_make = False
# for x in only_x :
#     total_length = len(x)
#     if (total_length % len(poly_a)) % len(poly_b) != 0 :
#         cannot_make = True
#         print(-1)
#         break
#     poly_a_length = total_length // len(poly_a)
#     poly_b_length = (total_length % len(poly_a)) // len(poly_b)

#     real_poly = ''
#     for _ in range(poly_a_length) :
#         real_poly += poly_a
#     for _ in range(poly_b_length) :
#         real_poly += poly_b
#     encoded_x.append(real_poly)

# if not cannot_make :

#     remake_board = []
#     result = ''
#     for b in board_origin :
#         if b != '.' :
#             result += b
#         else :
#             if result :
#                 remake_board.append(result)
#                 result = ''
#             remake_board.append('.')
#     if result :
#         remake_board.append(result)
    
#     idx = 0
#     answer = ''
#     for i in range(len(remake_board)) :
#         if remake_board[i] != '.' :
#             answer += encoded_x[idx]
#             idx += 1
#         else :
#             answer += '.'
        
#     print(answer)
