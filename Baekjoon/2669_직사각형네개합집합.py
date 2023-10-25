import sys

board = []
for i in range(101) :
    tmp = []
    for j in range(101) :
        tmp.append(0)
    board.append(tmp)

for _ in range(4) :
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            board[i][j] = 1

cnt = 0
for i in range(101) :
    cnt += (board[i].count(1))

print(cnt)