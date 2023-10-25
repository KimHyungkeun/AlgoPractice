# 230615 재풀이
import sys

# row : 가로 길이
# col : 세로 길이
row, col = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline().rstrip())

board = []
for _ in range(col+1) :
    pos_list = [0] * (row+1)
    board.append(pos_list)

# 1 : 북
# 2 : 남
# 3 : 서
# 4 : 동
shop_pos = []
for _ in range(n) :
    direct, pos = map(int, sys.stdin.readline().split())
    if direct == 1 :
        board[0][pos] = 1
    if direct == 2 :
        board[col][pos] = 1
    if direct == 3 :
        board[pos][0] = 1
    if direct == 4 :
        board[pos][row] = 1
    shop_pos.append((direct,pos))

mydir, mypos = map(int, sys.stdin.readline().split())
    
cnt = 0
for p in shop_pos :
    
    # 같은 방향내에 위치
    if mydir == p[0] :
        cnt += abs(mypos - p[1])

    # 남북으로 서로 마주 볼때
    if (mydir == 1 and p[0] == 2) or (mydir == 2 and p[0] == 1) :
        cnt += (col-1)
        cnt += min((mypos+p[1]), ((row-mypos) + (row-p[1])))
        cnt += 1

    # 동서로 서로 마주 볼때
    if (mydir == 3 and p[0] == 4) or (mydir == 4 and p[0] == 3) :
        cnt += (row-1)
        cnt += min((mypos+p[1]), ((col-mypos) + (col-p[1])))
        cnt += 1

    # 북 -> 서
    if mydir == 1 and p[0] == 3 :
        cnt += mypos
        cnt += (p[1]-1)
        cnt += 1

    # 북 -> 동
    if mydir == 1 and p[0] == 4 :  
        cnt += (row-mypos)
        cnt += (p[1]-1)
        cnt += 1

    # 남 -> 서
    if mydir == 2 and p[0] == 3 :
        cnt += mypos
        cnt += (col-p[1]-1)
        cnt += 1

    # 남 -> 동
    if mydir == 2 and p[0] == 4 :
        cnt += (row-mypos)
        cnt += (col-p[1]-1)
        cnt += 1

    # 서 -> 북
    if mydir == 3 and p[0] == 1 :
        cnt += mypos
        cnt += (p[1]-1)
        cnt += 1

    # 서 -> 남
    if mydir == 3 and p[0] == 2 :
        cnt += (col-mypos)
        cnt += (p[1]-1)
        cnt += 1

    # 동 -> 북
    if mydir == 4 and p[0] == 1 :
        cnt += mypos
        cnt += (row-p[1]-1)
        cnt += 1

    # 동 -> 남
    if mydir == 4 and p[0] == 2 :
        cnt += (col-mypos)
        cnt += (row-p[1]-1)
        cnt += 1

print(cnt)




# 230525 정답
# import sys

# row, col = map(int, sys.stdin.readline().split())

# # 1:북, 2:남, 3:서, 4:동
# pos_list = []
# real_pos_list = []
# n = int(sys.stdin.readline().rstrip())
# for _ in range(n) :
#     direction, pos = map(int, sys.stdin.readline().split())
#     if direction == 1 :
#         real_pos_list.append((0, pos))
#     if direction == 2 :
#         real_pos_list.append((col, pos))
#     if direction == 3 :
#         real_pos_list.append((pos, 0))
#     if direction == 4 :
#         real_pos_list.append((pos, row))
#     pos_list.append((direction, pos))
    

# guard_i, guard_j = 0,0
# guard_direct, guard_pos = map(int, sys.stdin.readline().split())
# if guard_direct == 1 :
#     guard_i, guard_j =0, guard_pos
# if guard_direct == 2 :
#     guard_i, guard_j = col, guard_pos
# if guard_direct == 3 :
#     guard_i, guard_j = guard_pos, 0
# if guard_direct == 4 :
#     guard_i, guard_j = guard_pos, row

# cnt = 0
# for i in range(len(pos_list)) :
#     # 같은 포지션상에 있다면 그 거리만 구하면 된다
#     if guard_direct == pos_list[i][0] :
#         cnt += abs(guard_pos - pos_list[i][1])
#     else :
#         if (guard_direct == 1 and pos_list[i][0] == 2) or (guard_direct == 2 and pos_list[i][0] == 1) :
#                 cnt += min( (guard_pos + pos_list[i][1] + col), (row-guard_pos + row-pos_list[i][1] + col) )

#         elif (guard_direct == 3 and pos_list[i][0] == 4) or (guard_direct == 4 and pos_list[i][0] == 3) :
#                 cnt += min( (col-guard_pos + col-pos_list[i][1] + row), (guard_pos + pos_list[i][1] + row) )

#         else :
#             cnt += (abs(real_pos_list[i][0] - guard_i)) + (abs(real_pos_list[i][1] - guard_j))

# print(cnt)



