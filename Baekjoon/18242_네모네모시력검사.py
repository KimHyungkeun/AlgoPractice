import sys

n, m = map(int, sys.stdin.readline().split())

board = []
for _ in range(n) :
    row = list(sys.stdin.readline().rstrip())
    board.append(row)

row_len_list = []
col_len_list = []

for r in board :
    if r.count('#') > 0 :
        row_len_list.append(r.count('#'))


# 상하좌우 각각의 길이에서, 최대측정 길이보다 1씩 작은 부분이 있다.
# 그 부분이 상에 있다면 UP, 하에 있다면 DOWN, 좌에 있다면 LEFT, 우에 있다면 RIGHT 이다
for i in range(m) :
    cnt = 0
    for j in range(n) :
        if board[j][i] == '#' :
            cnt += 1
    if cnt > 0 :
        col_len_list.append(cnt)

if row_len_list[0] > row_len_list[-1] :
    print("DOWN")

if row_len_list[0] < row_len_list[-1] :
    print("UP")

if col_len_list[0] > col_len_list[-1] :
    print("RIGHT")

if col_len_list[0] < col_len_list[-1] :
    print("LEFT")
