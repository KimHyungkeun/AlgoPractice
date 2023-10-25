# 230922 Retry Success
import sys

n = int(sys.stdin.readline().rstrip())

mine_pos = []
board = []
mine_cnt_board = []

dy = [0,0,-1,1,1,1,-1,-1]
dx = [1,-1,0,0,1,-1,1,-1]


for i in range(n) :
    row = list(sys.stdin.readline().rstrip())
    tmp = []
    for j in range(len(row)) :
        if row[j] != '.' :
            tmp.append(int(row[j]))
            mine_pos.append((i,j))
        else :
            tmp.append(0)
    mine_cnt_board.append(tmp)
    board.append(row)

for m in mine_pos :
    for t in range(8) :
        y = m[0] + dy[t]
        x = m[1] + dx[t]

        if 0 <= y < n and 0 <= x < n :
            mine_cnt_board[y][x] += int(board[m[0]][m[1]])

for i in range(n) :
    for j in range(n) :
        if board[i][j] != '.' :
            print('*', end='')
        elif mine_cnt_board[i][j] >= 10 :
            print('M', end='')
        else :
            print(mine_cnt_board[i][j], end='')
    print()


# 230909 4%에서 오답 
# import sys

# n = int(sys.stdin.readline().rstrip())
# board = []
# mine_location = []

# dy = [1,-1,0,0,1,-1,1,-1]
# dx = [0,0,1,-1,1,1,-1,-1]


# for i in range(n) :
#     row = list(sys.stdin.readline().rstrip())
#     for j in range(len(row)) :
#         if row[j] != '.' :
#             mine_location.append((i,j))
#         if row[j] == '.' :
#             row[j] = '0'
#     board.append(row)

# for m in mine_location :
#     y,x = m[0], m[1]
#     val = board[y][x]
#     for i in range(8) :
#         if (0 <= y + dy[i] < n) and (0 <= x + dx[i] < n) :
#             accumlate = int(board[y+dy[i]][x+dx[i]]) + int(val)
#             board[y+dy[i]][x+dx[i]] = str(accumlate) 

# while mine_location :
#     y, x = mine_location.pop()
#     print(y,x)
#     board[y][x] = '*'

# for b in board: 
#     for i in range(len(b)) :
#         if b[i] != '*' and int(b[i]) >= 10 :
#             b[i] = 'M'

# for b in board:
#     for i in range(len(b)) :
#         print(b[i],end='')
#     print()

# --------------------------------------------------

# 230911 4%에서 오답

# import sys

# n = int(sys.stdin.readline().rstrip())
# board = [[0] * n for _ in range(n)]

# dy = [1,-1,0,0,1,-1,1,-1]
# dx = [0,0,1,-1,1,1,-1,-1]
# mine_location = []

# for i in range(n) :
#     row = list(sys.stdin.readline().rstrip())
#     for j in range(n) :
#         if row[j] != '.' :
#             mine_location.append((i,j))
#             board[i][j] = int(row[j])

# for m in mine_location :
#     y,x = m[0], m[1]
#     val = board[y][x]
#     for i in range(8) :
#         if (0 <= y + dy[i] < n) and (0 <= x + dx[i] < n) :
#             board[y+dy[i]][x+dx[i]] += val

# while mine_location :
#     y, x = mine_location.pop()
#     board[y][x] = '*'

# for b in board: 
#     for i in range(len(b)) :
#         if b[i] != '*' and b[i] >= 10 :
#             b[i] = 'M'

# for b in board:
#     for i in range(len(b)) :
#         print(b[i],end='')
#     print()



# ----------------------------------------------------------------

# 정답코드 : https://velog.io/@vkdldjvkdnj/boj01996
# import sys; input = sys.stdin.readline

# N = int(input())
# matrix = [input().strip() for _ in range(N)]

# # 주위 지뢰의 개수를 저장할 행렬
# result = [[0] * N for _ in range(N)]

# # 12시 방향부터 시계 방향으로 8방향
# dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# # 지뢰가 있는 칸을 찾아 인접해 있는 칸에 지뢰 개수를 더하자.
# for i in range(N):
#     for j in range(N):
#         if matrix[i][j].isdigit(): # 숫자를 나타내는 문자라면 지뢰가 있는 칸이다.
#             n = int(matrix[i][j])
#             for di, dj in dir:
#                 if 0 <= i + di < N and 0 <= j + dj < N:
#                     result[i + di][j + dj] += n

# for i in range(N):
#     for j in range(N):
#         if matrix[i][j].isdigit(): # 지뢰가 있는 칸
#             print('*', end = '')
#         elif result[i][j] >= 10: # 주위 지뢰가 10개 이상
#             print('M', end = '')
#         else: # 주위 지뢰가 10개 미만
#             print(result[i][j], end = '')
#     print()

# --------------------------------------------------------------------

# 정답코드를 참고하여 다시 진행해본 답안
import sys

n = int(sys.stdin.readline().rstrip())
result = [[0] * n for _ in range(n)]
board = []

di = [1,-1,0,0,1,-1,1,-1]
dj = [0,0,1,-1,1,1,-1,-1]
mine_location = []

for i in range(n) :
    row = list(sys.stdin.readline().rstrip())
    board.append(row)

for i in range(n) :
    for j in range(n) :
        if board[i][j] != '.' :
            val = int(board[i][j])
            for d in range(8) :
                if (0 <= i + di[d] < n) and (0 <= j + dj[d] < n) :
                    result[i+di[d]][j+dj[d]] += val

for i in range(n) :
    for j in range(n) :
        if board[i][j] != '.' :
            result[i][j] = '*'
        elif result[i][j] >= 10 :
            result[i][j] = 'M'
        else :
            None

for r in result :
    for i in range(len(r)) :
        print(r[i], end='')
    print()