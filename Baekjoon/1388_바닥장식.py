import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n) :
    tmp = list(sys.stdin.readline().rstrip())
    board.append(tmp)

# 1. '-'가 필요한 갯수

row_cnt = 0
for i in range(n) :
    cnt = 0
    for j in range(m) :
        if board[i][j] == '-' :
            cnt += 1
        else :
            if cnt >= 1 :
                row_cnt += 1
            cnt = 0
    if cnt >= 1 :
        row_cnt += 1

# 2. '|'가 필요한 갯수

col_cnt = 0
for i in range(m) :
    cnt = 0
    for j in range(n) :
        if board[j][i] == '|' :
            cnt += 1
        else :
            if cnt >= 1 :
                col_cnt += 1
            cnt = 0
    if cnt >= 1 :
        col_cnt += 1

print(row_cnt + col_cnt) 